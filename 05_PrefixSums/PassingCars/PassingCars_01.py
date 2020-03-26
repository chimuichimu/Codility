# Score100% Time ComplexityはO(N)
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    count_zero = 0
    answer = 0
    
    for a in A:
        if a == 0:
            count_zero += 1
        else:
            answer += count_zero
    
    if answer > 1000000000:
        answer = -1
    
    return answer