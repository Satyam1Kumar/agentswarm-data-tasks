import {types as utilTypes} from 'node:util';


function isNormalDenseArray(value) {
  if (utilTypes.isProxy(value) || !Array.isArray(value)) {
    return false;
  }
  if (Object.getPrototypeOf(value) !== Array.prototype) {
    return false;
  }

  for (let index = 0; index < value.length; index += 1) {
    const descriptor = Object.getOwnPropertyDescriptor(value, String(index));
    if (!descriptor || !Object.hasOwn(descriptor, 'value')) {
      return false;
    }
  }
  return true;
}


export function histogram(values, edges) {
  if (!isNormalDenseArray(values) || !isNormalDenseArray(edges)) {
    throw new TypeError('values and edges must be normal dense arrays');
  }

  for (let index = 0; index < values.length; index += 1) {
    if (typeof values[index] !== 'number') {
      throw new TypeError('values must contain primitive numbers');
    }
  }
  for (let index = 0; index < edges.length; index += 1) {
    if (typeof edges[index] !== 'number') {
      throw new TypeError('edges must contain primitive numbers');
    }
  }

  for (let index = 0; index < values.length; index += 1) {
    if (!Number.isSafeInteger(values[index])) {
      throw new RangeError('values must contain safe integers');
    }
  }
  for (let index = 0; index < edges.length; index += 1) {
    if (!Number.isSafeInteger(edges[index])) {
      throw new RangeError('edges must contain safe integers');
    }
  }

  if (edges.length < 2) {
    throw new RangeError('edges must contain at least two integers');
  }
  for (let index = 1; index < edges.length; index += 1) {
    if (edges[index] <= edges[index - 1]) {
      throw new RangeError('edges must be strictly increasing');
    }
  }

  const counts = new Array(edges.length - 1).fill(0);
  const finalEdge = edges[edges.length - 1];
  const finalBin = counts.length - 1;

  for (let index = 0; index < values.length; index += 1) {
    const value = values[index];
    if (value < edges[0] || value > finalEdge) {
      continue;
    }
    if (value === finalEdge) {
      counts[finalBin] += 1;
      continue;
    }

    let low = 0;
    let high = edges.length;
    while (low < high) {
      const middle = Math.floor((low + high) / 2);
      if (edges[middle] <= value) {
        low = middle + 1;
      } else {
        high = middle;
      }
    }
    counts[low - 1] += 1;
  }

  return counts;
}
