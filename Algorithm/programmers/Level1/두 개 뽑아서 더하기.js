function solution(numbers) {
  let answer = [];
  for (let i = 0; i < numbers.length - 1; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      let num = numbers[i] + numbers[j];
      if (!answer.includes(num)) answer.push(num);
    }
  }
  return answer.sort((a, b) => a - b);
}

function solution(numbers) {
  let answer = new Set();
  for (let i = 0; i < numbers.length - 1; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      answer.add(numbers[i] + numbers[j]);
    }
  }
  return [...answer].sort((a, b) => a - b);
}
