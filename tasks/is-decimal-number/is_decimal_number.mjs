const DECIMAL_NUMBER = /^-?(0|[1-9][0-9]*)(\.[0-9]+)?$/;

export function isDecimalNumber(text) {
  if (typeof text !== "string") {
    throw new TypeError("text must be a primitive string");
  }
  if (text.length > 1000) {
    throw new RangeError("text must be at most 1000 UTF-16 code units");
  }
  return DECIMAL_NUMBER.test(text);
}
