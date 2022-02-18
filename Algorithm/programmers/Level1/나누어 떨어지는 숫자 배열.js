function solution(arr, divisor) {
  var answer = [];
  // 오름차순 정렬
  arr.sort((a, b) => a - b);
  arr.forEach((v) => {
    if (v % divisor === 0) answer.push(v);
  });
  return answer.length > 0 ? answer : [-1];
}

function solution(arr, divisor) {
  let answer = arr.filter((v) => v % divisor === 0);
  return answer.length > 0 ? answer.sort((a, b) => a - b) : [-1];
}
