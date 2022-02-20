function solution(arr) {
  let getGCD = (num1, num2) => {
    let gcd = 1;

    for (let i = 2; i <= Math.min(num1, num2); i++) {
      if (num1 % i === 0 && num2 % i === 0) {
        gcd = i;
      }
    }

    return gcd;
  };

  let answer = arr[0];

  for (let i = 1; i < arr.length; i++) {
    answer = (answer * arr[i]) / getGCD(answer, arr[i]);
  }

  return answer;
}
