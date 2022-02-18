function solution(strings, n) {
  let answer = [];

  for (let i = 0; i < strings.length; i++) {
    strings[i] = strings[i][n] + strings[i];
  }

  strings.sort();

  for (let i = 0; i < strings.length; i++) {
    answer.push(strings[i].substring(1));
  }
  return answer;
}
