def solution(s):
    p_count = 0
    y_count = 0
    for char in s.lower():
        if char == 'p':
            p_count += 1
        elif char == 'y':
            y_count += 1

    if p_count - y_count == 0:
        return True
    else:
        return False

def solution(s):
    return s.lower().count('p') == s.lower().count('y')