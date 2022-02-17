function solution(s, n) {
  var answer = [];
  let pattern1 = /[a-z]/;
  let pattern2 = /[A-Z]/;
  for (let i = 0; i < s.length; i++) {
    let code = s.charCodeAt(i);
    if (pattern2.test(s[i])) {
      // 대문자인 경우
      answer.push(String.fromCharCode(65 + ((code - 65 + n) % 26)));
    } else if (pattern1.test(s[i])) {
      // 소문자인 경우
      answer.push(String.fromCharCode(97 + ((code - 97 + n) % 26)));
    } else {
      // 공백인 경우
      answer.push(String.fromCharCode(code));
    }
  }
  return answer.join("");
}
