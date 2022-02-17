function solution(n) {
  var answer = "";
  for (let i = 0; i < n; i++) {
    if (i % 2 === 0) answer += "수";
    else answer += "박";
  }
  return answer;
}

function solution(n) {
  if (n === 1) {
    return "수";
  } else {
    return n % 2 === 0 ? "수박".repeat(n / 2) : "수박".repeat(n / 2) + "수";
  }
}

function solution(n) {
  return "수박".repeat(n).slice(0, n);
}
