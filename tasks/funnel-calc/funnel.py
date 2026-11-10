"""Compute unique AARRR stage counts by channel and UTC day from a CSV."""

import argparse
import csv
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path


STAGES = ("acquisition", "activation", "referral", "revenue")
COUNT_STAGES = ("acquisition", "activation", "retention", "referral", "revenue")
RETENTION_WINDOW = timedelta(days=7)


def _parse_timestamp(value):
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    instant = datetime.fromisoformat(value)
    return instant.astimezone(timezone.utc)


def _read_internal_actors(path):
    if path is None:
        return set()
    return {line for line in path.read_text(encoding="utf-8").splitlines() if line}


def _build_report(events, internal_actors):
    rows = []
    spammed = set()
    for row in events:
        actor = row["actor"]
        if actor in internal_actors:
            continue
        instant = _parse_timestamp(row["ts"])
        day = instant.date().isoformat()
        channel = row["channel"]
        event = row["event"]
        rows.append((instant, day, channel, actor, event))
        if event == "spam":
            spammed.add((day, channel, actor))

    groups = {}
    activation_groups = {}
    for instant, day, channel, actor, event in rows:
        if event not in STAGES:
            continue

        group_key = (day, channel)
        stages = groups.setdefault(group_key, {stage: set() for stage in COUNT_STAGES})
        actor_key = (day, channel, actor)

        if event == "acquisition":
            stages[event].add(actor)
        elif actor_key not in spammed:
            stages[event].add(actor)
            if event == "activation":
                activation_groups.setdefault((actor, instant), set()).add(group_key)

    activations_by_actor = {}
    for actor, instant in activation_groups:
        activations_by_actor.setdefault(actor, []).append(instant)

    for actor, instants in activations_by_actor.items():
        instants.sort()
        for index in range(1, len(instants)):
            earlier = instants[index - 1]
            current = instants[index]
            if current - earlier <= RETENTION_WINDOW:
                for group_key in activation_groups[(actor, current)]:
                    groups[group_key]["retention"].add(actor)

    report = []
    for day, channel in sorted(groups):
        stages = groups[(day, channel)]
        report.append(
            {
                "day": day,
                "channel": channel,
                "acquisition": len(stages["acquisition"]),
                "activation": len(stages["activation"]),
                "retention": len(stages["retention"]),
                "referral": len(stages["referral"]),
                "revenue": len(stages["revenue"]),
            }
        )
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("events_csv", type=Path)
    parser.add_argument("--internal-actors", type=Path)
    args = parser.parse_args()

    internal_actors = _read_internal_actors(args.internal_actors)
    with args.events_csv.open(encoding="utf-8", newline="") as stream:
        report = _build_report(csv.DictReader(stream), internal_actors)
    print(json.dumps(report, ensure_ascii=False, separators=(",", ":")))


if __name__ == "__main__":
    main()
