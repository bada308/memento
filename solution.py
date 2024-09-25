# 1번 문제) 제일 작은 수 제거하기

def solution(arr):
    if len(arr) == 1:
        return [-1]
    answer = []
    min_num = min(arr)
    for a in arr:
        if a != min_num: answer.append(a)
    return answer

print(solution([4, 3, 2, 1]))
print(solution([10]))