function solution(seoul) {
  let answer = "";
  seoul.map((v, i) => {
    if (v === "Kim") answer = "김서방은 " + i + "에 있다";
  });

  return answer;
}

function solution(seoul) {
  return "김서방은 " + seoul.indexOf("Kim") + "에 있다";
}
