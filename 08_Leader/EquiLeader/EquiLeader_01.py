# Score 55% Time Complexity O(N**2)
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections

def solution(A):
    count_equi_leaders = 0
    
    for idx in range(0,len(A)-1):
        # リストAを左右のリストに分割
        left  = A[0    :idx+1 ]
        right = A[idx+1:len(A)]
        
        # 左右それぞれの最頻値を取得
        left_c = collections.Counter(left)
        left_mode = left_c.most_common(1)
        right_c = collections.Counter(right)
        right_mode = right_c.most_common(1)
        
        # 左右それぞれの最頻値がリストの要素数の半数を上回り、
        # かつ左右で等しいときにカウント
        if left_mode[0][1]  > len(left)  / 2 and \
           right_mode[0][1] > len(right) / 2 and \
           left_mode[0][0] == right_mode[0][0]:
            count_equi_leaders += 1
    
    return count_equi_leaders