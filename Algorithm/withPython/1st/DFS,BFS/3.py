# 괄호 변환
# 균형잡힌 문자열로 분리하기 위한 인덱스를 얻는 함수
def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

# 올바른 괄호 문자열인지 확인하는 함수
def check(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)  # 균형잡힌 문자열로 분리하기 위한 인덱스 추출
    u = p[:index + 1]
    v = p[index + 1:]
    # 분리한 문자열 u가 올바른 문자열인 경우
    if check(u):
        answer = u + solution(v)
    # 분리한 문자열 u가 올바른 문자열이 아닌 경우
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])  # 처음과 마지막 문자 제거 후
        # 괄호 방향 뒤집기
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)  # 뒤집은 결과를 뒤에 붙이기

    return answer


if __name__ == '__main__':
    assert solution("(()())()") == "(()())()"
    assert solution(")(") == "()"
    assert solution("()))((()") == "()(())()"
    print('OK')


# 다른 사람 풀이, lambda 함수를 이용한 방법
def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))


"""
접근 방법
- 문제에 요구하는 알고리즘이 나와있기 때문에 재귀적으로 구현
- 균형잡힌 괄호 문자열로 분리하기 위한 인덱스를 얻는 함수와 올바른 괄호 문자열인지를 판단하는 함수를 별도로 구현
- 입력된 문자열을 두 문자열(u, v)로 분리하는데 u는 균형잡힌 괄호 문자열로 더이상 분리할 수 없어야 하므로 왼쪽 괄호의 수를 더하고 오른쪽 괄호의 수를 빼면서
0이 될 때까지 실행하고 그때의 인덱스를 리턴한다.
- 그렇게 분리된 u가 올바른 괄호 문자열이라면 v에 대해 재귀적으로 호출하여 결과를 u 뒤에 더해주고
- u가 올바른 괄호 문자열이 아니라면 문제에서 요구하는대로 처리해준다.   
"""