function solution(n) {
  let answer = [];
  let tmp = String(n).split("").reverse();
  tmp.forEach((data) => answer.push(Number(data)));
  return answer;
}

function solution(n) {
  let answer = String(n).split("").reverse();
  return answer.map((data) => parseInt(data));
}
