# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if len(A) == 0:
        return 0
 
    A.sort()
    cnt = 1
    last_value = A[0]
 
    for idx in range(1, len(A)):
        if A[idx] != last_value:
            cnt += 1
            last_value = A[idx]
 
    return cnt