def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        tmp = ''  # 압축된 문자열을 저장할 빈 문자열
        count = 1
        prev = s[:step]  # 앞에서부터 step만큼 비교할 문자열 추출
        # step 크기만큼 증가시키면서 prev와 비교
        for j in range(step, len(s), step):
            # 이전 문자열과 step만큼 증가한 문자열이 같다면(압축 가능하다면) 카운팅
            if prev == s[j:j+step]:
                count += 1
            # 다른 문자열이 나왔다면(압축이 불가능 하다면)
            else:
                # 카운팅된 문자열이 1보다 크면
                if count > 1:
                    tmp += str(count) + prev  # 숫자+문자열
                else:
                    tmp += prev  # 카운팅된 문자열이 한 개라면 문자열
                count = 1
                prev = s[j:j+step]  # 중복이 끝난 문자열 바로 다음 문자열을 비교할 문자열로 재설정
        # 남아있는 문자열에 대해 처리
        tmp += str(count) + prev if count > 1 else prev
        answer = min(answer, len(tmp))

    return answer



if __name__ == '__main__':
    assert solution("aabbaccc") == 7
    assert solution("ababcdcdababcdcd") == 9
    assert solution("abcabcdede") == 8
    assert solution("abcabcabcabcdededededede") == 14
    assert solution("xababcdcdababcdcd") == 17
    print('OK')


"""
접근 방법
- 입력이 1000이하이기 때문에 완전 탐색으로 수행할 수 있다.
- 길이가 N인 문자열이 입력됐다면 1부터 2/N까지의 모든 수를 단위로 하여 문자열을 압축하는 방법을 모두 확인하고 그 중 최솟값 출력
"""