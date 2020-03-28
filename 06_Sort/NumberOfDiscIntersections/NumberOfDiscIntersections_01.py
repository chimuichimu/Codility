# Score56% Coorrectnessは100%だけど、Performanceが出ていない
# １つのディスクについて、そのディスクより後続のディスクたちを調べて接しているかを調べる、一番単純なやり方
# この方法だとTime ComplexityはO(N^2)
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    N = len(A)
    answer = 0
    
    for i in range(0,N-1):
        for j in range(i+1, N):
            if j-i <= A[i] + A[j]:
                answer += 1
    
    if answer > 10000000:
        answer = -1
    
    return answer