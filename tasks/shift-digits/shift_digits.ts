export function shiftDigits(text: unknown): string {
  if (typeof text !== "string") {
    throw new TypeError("text must be a primitive string");
  }
  if (text.length > 1000) {
    throw new RangeError("text may contain at most 1000 UTF-16 code units");
  }

  return text.replace(/[0-9]/g, (digit) => {
    const value = digit.charCodeAt(0) - 48;
    return String.fromCharCode(48 + ((value + 1) % 10));
  });
}
