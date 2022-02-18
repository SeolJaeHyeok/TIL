function solution(price, money, count) {
  let sumMoney = 0;
  for (let i = 1; i <= count; i++) {
    sumMoney += price * i;
  }

  return sumMoney > money ? sumMoney - money : 0;
}
