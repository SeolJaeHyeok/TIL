function solution(n) {
  var answer = 10000001;
  for (let i = n; i > 0; i--) {
    if (n % i === 1) answer = Math.min(answer, i);
  }
  return answer;
}

function solution(n) {
  for (let i = 2; i <= n; i++) {
    if (n % i === 1) return i;
  }
}
