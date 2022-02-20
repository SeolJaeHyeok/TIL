function solution(s) {
  let answer = [];
  let arr = s.split("");

  for (let val of arr) {
    if (val === answer[answer.length - 1]) answer.pop();
    else answer.push(val);
  }

  return answer.length === 0 ? 1 : 0;
}
