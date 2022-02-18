function solution(left, right) {
  let answer = 0;

  for (let i = left; i <= right; i++) {
    let num = 1;
    let mod = 1;
    while (mod <= i / 2) {
      if (i % mod === 0) num += 1;
      mod += 1;
    }
    if (num % 2 === 0) answer += i;
    else answer -= i;
  }
  return answer;
}

function solution(left, right) {
  let answer = 0;

  for (let i = left; i <= right; i++) {
    if (Number.isInteger(Math.sqrt(i))) answer -= i;
    else answer += i;
  }

  return answer;
}
