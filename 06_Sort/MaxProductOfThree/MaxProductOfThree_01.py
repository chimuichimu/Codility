# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()
    N = len(A)
    
    if A[1] >= 0:
        answer = A[N-1] * A[N-2] * A[N-3]
    else:
        answer = max(A[N-1] * A[N-2] * A[N-3], A[0] * A[1] * A[N-1])
    
    return answer