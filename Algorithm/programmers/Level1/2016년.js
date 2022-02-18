function solution(a, b) {
  let idx = 0;
  let daysName = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"];
  let daysNum = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

  for (let i = 0; i < a - 1; i++) {
    idx += daysNum[i];
  }

  return daysName[(idx + b - 1) % 7];
}
