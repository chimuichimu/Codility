# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections


def solution(A):
    
    if len(A) == 0:
        return -1
    
    # リストから最頻値を取得する。mode = [(最頻値), （出現回数）]
    c = collections.Counter(A)
    mode = c.most_common(1)
    
    # 要素数の半数より出現回数が多いとき、最頻値のインデックスを返す。
    # どのインデックスでもよいが、ここでは一番最初のインデックスを返す。
    if mode[0][1] > len(A) / 2:
        return A.index(mode[0][0])
    else:
        return -1