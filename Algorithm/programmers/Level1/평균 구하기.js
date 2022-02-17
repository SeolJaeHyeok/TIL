function solution(arr) {
  var answer = arr.reduce((prev, next) => prev + next);

  return answer / arr.length;
}
