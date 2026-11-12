/** Return whether text is a plain, checksum-valid ISBN-10. */
export function isIsbn10(text) {
  if (typeof text !== 'string') {
    throw new TypeError('text must be a primitive string');
  }
  if (text.length > 1000) {
    throw new RangeError('text must not exceed 1000 UTF-16 code units');
  }
  if (text.length !== 10) {
    return false;
  }

  let sum = 0;
  for (let i = 0; i < 9; i += 1) {
    const code = text.charCodeAt(i);
    if (code < 48 || code > 57) {
      return false;
    }
    sum += (10 - i) * (code - 48);
  }

  const checkCode = text.charCodeAt(9);
  if (checkCode >= 48 && checkCode <= 57) {
    sum += checkCode - 48;
  } else if (checkCode === 88) {
    sum += 10;
  } else {
    return false;
  }

  return sum % 11 === 0;
}
