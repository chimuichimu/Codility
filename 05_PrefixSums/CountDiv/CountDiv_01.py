# Score87% ロジックにミスあり
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    
    if A%K != 0 and B%K != 0:
        cnt = (B-A) // K
    else:
        cnt = (B-A) // K + 1
    
    return cnt