function solution(n) {
  var tmp = String(n).split("");
  let answer = tmp.sort().reverse().join("");
  return Number(answer);
}
