function solution(num) {
  var answer = 0;

  while (num !== 1) {
    if (answer >= 500) break;

    let check = num % 2 === 0;

    if (check) {
      num /= 2;
    } else {
      num = num * 3 + 1;
    }
    answer += 1;
  }

  return num === 1 ? answer : -1;
}

function solution(num) {
  var answer = 0;

  while (num !== 1) {
    if (answer >= 500) break;
    num % 2 === 0 ? (num /= 2) : (num = num * 3 + 1);
    answer += 1;
  }

  return num === 1 ? answer : -1;
}
