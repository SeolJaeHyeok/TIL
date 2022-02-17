function solution(n) {
  let answer = Math.sqrt(n);
  return answer % 1 === 0 ? (answer + 1) ** 2 : -1;
}
