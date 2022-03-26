"""
당신은 로그 수집 프로그램을 만들게 되었습니다.
특정 조건들을 만족한 로그만을 수집해야 하며 그 외의 로그는 수집하지 않아야 합니다.

조건은 다음과 같습니다.

로그는 "team_name : t application_name : a error_level : e message : m" 형식이어야 합니다.
t, a, e, m은 알파벳 소문자 혹은 알파벳 대문자로만 이루어진 길이 1 이상의 문자열입니다.
team_name, application_name, error_level, message, :, t, a, e, m는 한 칸의 공백으로 구분되어 있어야 합니다.
로그의 길이는 100 이하여야 합니다.
로그 수집 프로그램으로 분석할 로그들이 담긴 문자열 배열 logs가 매개변수로 주어졌을 때,
logs에 담긴 로그 중 수집하지 않는 로그의 개수를 return 하도록 solution 함수를 완성해주세요.

Input
["team_name : db application_name : dbtest error_level : info message : test",
"team_name : test application_name : I DONT CARE error_level : error message : x",
"team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever",
"team_name : oberervability application_name : LogViewer error_level : error"]

제한 사항
1 ≤ logs의 길이 ≤ 100
1 ≤ logs의 원소 길이 ≤ 200
logs의 원소는 알파벳, 숫자, 공백, 특수 문자로 이루어져 있습니다.

Output
3

Input
["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange",
"no such file or directory",
"team_name : recommend application_name : recommend error_level : info message : RecommendSucces11",
"team_name : recommend application_name : recommend error_level : info message : Success!",
"   team_name : db application_name : dbtest error_level : info message : test",
"team_name     : db application_name : dbtest error_level : info message : test",
"team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]

Output
6
"""
def solution(logs):
    answer = 0
    table = {
        0: 'team_name',
        1: 'application_name',
        2: 'error_level',
        3: 'message'
    }
    for log in logs:
        # 로그 길이 100 초과
        if len(log) > 100:
            answer += 1
            continue

        target = log.split(" : ")
        target = ''.join(target)
        target = target.split(' ')

        # 올바른 로그가 아닌 경우
        if len(target) != 4:
            answer += 1
            continue

        for i in range(len(target)):
            flag = False
            for j in range(4):
                # 올바른 로그 이름이 포함되어 있지 않은 경우
                if target[i].find(table[j]) == -1:
                    flag = True
                    break

            if flag:
                answer += 1
                break

    return answer - 1

solution(["team_name : db application_name : dbtest error_level : info message : test",
"team_name : test application_name : I DONT CARE error_level : error message : x",
"team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever",
"team_name : oberervability application_name : LogViewer error_level : error"])
solution(["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"])