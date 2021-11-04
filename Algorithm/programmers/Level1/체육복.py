# 90/100
def solution(n, lost, reserve):
    check = [1] * (n + 1)
    for i in lost:
        check[i] -= 1
    for i in reserve:
        check[i] += 1

    for i in reserve:

        if i - 1 in lost and not check[i - 1] and check[i] == 2:
            check[i - 1] += 1
            check[i] -= 1
        elif i + 1 in lost and not check[i + 1] and check[i] == 2:
            check[i + 1] += 1
            check[i] -= 1

    total = check.count(1) + check.count(2) - 1
    return total

# 100/100
def solution(n, lost, reserve):
    _reserve = set(reserve) - set(lost)
    _lost = set(lost) - set(reserve)

    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(r - 1)
        elif b in _lost:
            _lost.remove(r + 1)

    return n - len(_lost)