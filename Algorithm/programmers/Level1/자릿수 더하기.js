function solution(n) {
  let answer = 0;
  var arr = n.toString().split("");
  arr.map((data) => (answer += parseInt(data)));
  return answer;
}

function solution(n) {
  let answer = n.toString().split("");
  return answer.reduce((prev, next) => prev + parseInt(next), 0);
}
