function solution(nums) {
  let max = nums.length / 2;
  let arr = [...new Set(nums)];

  return arr.length > max ? max : arr.length;
}
