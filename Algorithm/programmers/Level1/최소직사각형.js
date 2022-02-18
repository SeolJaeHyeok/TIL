function solution(sizes) {
  let width = [];
  let height = [];

  for (let size of sizes) {
    size.sort((a, b) => a - b);
    width.push(size[1]);
    height.push(size[0]);
  }

  return Math.max(...width) * Math.max(...height);
}
