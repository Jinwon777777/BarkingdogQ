def solution(n):
    answer = []
    while n >=10:
        answer.append(n%10)
        n=n//10
    if n > 0:
        answer.append(n)
    return answer