function solution(x) {
  x = x + "";
  let mod = 0;
  for (let i = 0; i < x.length; i++) {
    mod += Number(x[i]);
  }

  return Number(x) % mod === 0;
}
