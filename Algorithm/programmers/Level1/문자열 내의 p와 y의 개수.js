function solution(s) {
  let pCount = 0;
  let yCount = 0;

  s.split("").map((v) => {
    if (v.toLowerCase() === "p") pCount += 1;
    else if (v.toLowerCase() === "y") yCount += 1;
  });

  return pCount === yCount;
}

function solution(s) {
  let count = 0;
  s.split("").map((v) => {
    if (v.toLowerCase() === "p") count += 1;
    else if (v.toLowerCase() === "y") count -= 1;
  });

  return count === 0 ? true : false;
}
