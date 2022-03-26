"""
문제
표 편집 프로그램을 통해서 셀의 너비를 원하는 대로 조절하려고 합니다.
아래 그림의 위쪽 셀들은 초기 상태의 셀들이며, 초기 상태 셀들의 너비를 화살표 아래쪽 셀들의 너비처럼 조절하려고 합니다.

셀의 너비는 셀끼리 인접한 경계선을 움직여서 조절합니다. 한쪽 셀의 너비를 줄이면 그만큼 인접한 셀의 너비가 늘어납니다.
모든 초기 셀의 너비는 1이 될 때까지 줄일 수 있지만, 셀을 지우거나 생성할 수는 없습니다.

위 그림의 셀은 아래 그림처럼 총 3번의 조절로 원하는 너비로 바꿀 수 있습니다.

초기 셀들의 너비를 담고 있는 정수 배열 arr과 원하는 셀들의 너비를 담고 있는 정수 배열 brr이 매개변수로 주어집니다.
초기 셀들의 너비를 원하는 너비로 바꾸기 위한 최소 조절 횟수를 return 하도록 solution 함수를 완성해주세요.

제한사항
2 ≤ arr 길이 = brr 길이 ≤ 300,000
1 ≤ arr의 원소, brr의 원소 ≤ 250
arr의 원소의 합 = brr의 원소의 합 ≤ 10,000,000

Input
[3, 7, 2, 4] [4, 5, 5, 2]
Output
3

Input
[6, 2, 2, 6] [4, 4, 4, 4]
Output
2
"""
def solution(arr, brr):
    answer = 0
    for i in range(len(arr) - 1):
        if arr[i] != brr[i]:
            dif = abs(arr[i] - brr[i])
            flag = arr[i] > brr[i]

            if flag:
                arr[i] -= dif
                arr[i + 1] += dif
                answer += 1
            else:
                arr[i] += dif
                arr[i + 1] -= dif
                answer += 1

    return answer