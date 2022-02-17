function solution(s) {
  if (s.length === 4 || s.length === 6) {
    if (Number(s)) return true;
    else return false;
  }
  return false;
}

function solution(s) {
  let tmp = parseInt(s);
  if (s.length === 4 || s.length === 6) {
    if (s == tmp) return true;
  }
  return false;
}
