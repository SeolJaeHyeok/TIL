def solution(time, plans):
    for plan in plans:
        ar, s, e = plan[0], plan[1], plan[2]
        start = int(s[:-2]) if s[-2:] == 'AM' else int(s[:-2]) + 12
        end = int(e[:-2]) if e[-2:] == 'AM' else int(e[:-2]) + 12

        total = (18 - start) + (end - 13)

        if total < time:
            return ar
