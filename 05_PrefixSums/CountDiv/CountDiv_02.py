# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):

    min_value =  ((A + K -1) // K) * K
 
    if min_value > B:
      return 0
 
    return ((B - min_value) // K) + 1