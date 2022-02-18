function solution(d, budget) {
  var answer = 0;
  d.sort((a, b) => a - b);
  for (let money of d) {
    budget -= money;
    if (budget < 0) break;
    answer += 1;
  }
  return answer;
}
