function solution(arr) {
  const minValue = Math.min(...arr);

  return arr.length === 1 ? [-1] : arr.filter((v) => v !== minValue);
}

function solution(arr) {
  const minValue = Math.min(...arr);
  const idx = arr.indexOf(minValue);
  arr.splice(idx, 1);

  return arr.length === 1 ? [-1] : arr;
}
