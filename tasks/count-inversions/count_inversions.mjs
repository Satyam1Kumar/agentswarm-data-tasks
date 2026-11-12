import { types } from "node:util";

export function countInversions(values) {
  if (
    types.isProxy(values) ||
    !Array.isArray(values) ||
    Object.getPrototypeOf(values) !== Array.prototype
  ) {
    throw new TypeError("values must be a normal Array, not a proxy or subclass");
  }

  const length = values.length;
  for (let index = 0; index < length; index += 1) {
    if (!Object.hasOwn(values, index) || typeof values[index] !== "number") {
      throw new TypeError("values must be dense and contain primitive numbers");
    }
  }

  if (length > 1000) {
    throw new RangeError("values may contain at most 1000 elements");
  }
  for (let index = 0; index < length; index += 1) {
    const value = values[index];
    if (!Number.isInteger(value) || Math.abs(value) > 1_000_000_000) {
      throw new RangeError("values must be bounded integers");
    }
  }

  let count = 0;
  for (let left = 0; left < length; left += 1) {
    for (let right = left + 1; right < length; right += 1) {
      if (values[left] > values[right]) {
        count += 1;
      }
    }
  }
  return count;
}
