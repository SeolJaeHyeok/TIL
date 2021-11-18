def solution(skill, skill_trees):
    count = len(skill_trees)
    for s in skill_trees:
        tmp = []
        for i in s:
            if i in skill:
                tmp.append(i)

        for idx, sk in enumerate(tmp):
            # print(idx, sk)
            if sk != skill[idx]:
                count -= 1
                break

    return count
