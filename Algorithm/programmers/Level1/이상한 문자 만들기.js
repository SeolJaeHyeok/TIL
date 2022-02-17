function solution(s) {
  let answer = [];
  let tmp = s.split(" ");

  for (let i = 0; i < tmp.length; i++) {
    let str = "";
    for (let j = 0; j < tmp[i].length; j++) {
      if (j % 2 === 0) str += tmp[i][j].toUpperCase();
      else str += tmp[i][j].toLowerCase();
    }
    answer.push(str);
  }

  return answer.join(" ");
}
