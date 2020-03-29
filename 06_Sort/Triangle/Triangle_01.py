# Score100% TimeComplexityはO(N*log(N))
# ソート後のリストAについて、連続する３つの要素(A[i-2], A[i-1], A[i])を考える。
# 昇順に並んでいるのでA[i] + A[i-1] > A[i-2] とA[i] + A[i-2] > A[i-1]は常に成り立つ。
# よってA[i-1] + A[i-2] > A[i]が成り立つ組み合わせがあるかを調べる。
# 昇順で並んでいるので、A[i-1] と A[i-2]で上記の関係が成り立たないならば、
# A[i-3], A[i-4],,,の要素を使った組み合わせでも成り立たないので、i-2,i-1,iだけについて調べればよい。
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    
    is_exist = 0
    N = len(A)
    if N < 3:
        return is_exist
   
    A.sort()
    for i in range(2,N):
        if A[i-2] + A[i-1] > A[i]:
            is_exist = 1
    
    return is_exist