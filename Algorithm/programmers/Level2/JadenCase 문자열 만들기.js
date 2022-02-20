function solution(s) {
  let arr = s.split(" ");
  let answer = [];

  for (let str of arr) {
    str = str.toLowerCase();
    if (str) {
      str = str[0].toUpperCase() + str.slice(1);
    }
    answer.push(str);
  }

  return answer.join(" ");
}

function solution(s) {
  return s
    .split(" ")
    .map((v) => v.charAt(0).toUpperCase() + v.substring(1).toLowerCase())
    .join(" ");
}
