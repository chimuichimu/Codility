# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections

def solution(A):
    count_equi_leaders = 0
    count_mode = 0
    
    # リストの最頻値と出現回数を取得
    mode = collections.Counter(A).most_common(1)
    
    for idx in range(0,len(A)-1):
        if A[idx] == mode[0][0]:
            count_mode += 1
        
        if count_mode > (idx + 1) / 2 and (mode[0][1] - count_mode) > (len(A)-1-idx) / 2:
            count_equi_leaders += 1
    
    return count_equi_leaders