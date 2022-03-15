const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let n = 0;

rl.on("line", function (x) {
  n = parseInt(x);
  rl.close();
}).on("close", function () {
  let array = [];
  // x, y 좌표의 현재 위치, 시작, 끝 값
  let x = { cur: 0, start: 0, end: n - 1 };
  let y = { cur: 0, start: 0, end: n - 1 };
  let dir = 1; // 방향
  let now = "y"; // 현재 변화하고 있는 축

  // 배열 초기화
  for (let i = 0; i < n; i++) {
    array.push([]);
  }

  for (let i = 0; i < n * n; i++) {
    array[x.cur][y.cur] = i + 1; // 현재 위치에 값 넣기
    if (now === "y") {
      // Y축 변화일 경우
      y.cur += dir;
      if (dir > 0 && y.cur === y.end) {
        // Y축이 end와 만났을 경우
        now = "x"; // 축 변환
        x.start += dir; // 이동
      } else if (dir < 0 && y.cur === y.start) {
        // Y축이 start와 만났을 경우
        now = "x";
        x.end += dir;
      }
    } else {
      // X축 변화일 경우
      x.cur += dir;
      if (dir > 0 && x.cur === x.end) {
        // X축이 end와 만났을 경우
        now = "y";
        dir = -1; // 방향 전환
        y.end += dir;
      } else if (dir < 0 && x.cur === x.start) {
        // X축이 start와 만났을 경우
        now = "y";
        dir = 1; // 방향 전환
        y.start += dir;
      }
    }
  }

  for (let i = 0; i < n; i++) {
    console.log(...array[i]);
  }
  process.exit();
});
"""
5

   1     2     3     4     5
  16    17    18    19     6
  15    24    25    20     7
  14    23    22    21     8
  13    12    11    10     9
"""
