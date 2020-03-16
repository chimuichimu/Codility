# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    
    # define initial counters
    cnts = [0] * N
    
    # define max counter
    max_cnt = 0
    
    # let counters operate
    for a in A:
        if a >= 1 and a <= N:
            cnts[a-1] += 1
            max_cnt = max(max_cnt, cnts[a-1])
        else:
            cnts = [max_cnt] * N
            
    return cnts