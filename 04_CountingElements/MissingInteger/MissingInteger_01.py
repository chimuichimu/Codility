# スコア100% まず昇順にソートしてから、１個ずつ要素をみて値を更新する
# time complexityはO(N) or O(N * log(N))
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    answer = 1
    A.sort()

    for e in A:
        if e == answer:
            answer += 1
        else:
            pass
    
    return answer