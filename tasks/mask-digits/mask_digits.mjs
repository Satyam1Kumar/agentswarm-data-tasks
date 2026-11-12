export function maskDigits(text) {
  if (typeof text !== "string") {
    throw new TypeError("text must be a primitive string");
  }
  if (text.length > 1000) {
    throw new RangeError("text may contain at most 1000 UTF-16 code units");
  }
  return text.replace(/[0-9]/g, "*");
}
