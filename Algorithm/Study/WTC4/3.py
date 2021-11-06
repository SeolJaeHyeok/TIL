def solution(ings, menu, sell):
    answer = 0
    # 재료비 테이블
    table = {}
    for i in ings:
        m, p = i.split(' ')
        table[m] = int(p)

    # 메뉴당 하나 당 수익 테이블
    menu_table = {}
    for i in menu:
        name, mat, sell_price = i.split(' ')
        menu_price = 0  # 각 메뉴의 총 재료비
        # 재료비 계산
        for m in mat:
            menu_price += table[m]
        menu_table[name] = int(sell_price) - menu_price  # 수익 = 판매가 - 재료비

    # 실적 테이블
    for i in sell:
        name, num = i.split(' ')
        answer += (menu_table[name] * int(num))

    return answer