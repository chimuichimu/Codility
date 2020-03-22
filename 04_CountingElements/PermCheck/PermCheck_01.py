# Score100% 配列をソートしたうえ、enumerateを用いてリストの要素とインデックスを取り出し、比較する
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    # 配列を昇順にソート
    A.sort()
    answer = 1
    
    # 各要素とインデックスを比較し、Permutationか否かをチェックする
    for index, e in enumerate(A):
        if e == index + 1:
            pass
        else:
            answer = 0
            break

    return answer