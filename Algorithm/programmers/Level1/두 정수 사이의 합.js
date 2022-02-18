function solution(a, b) {
  return a > b ? ((a - b + 1) * (a + b)) / 2 : ((b - a + 1) * (a + b)) / 2;
}
