# 改善版　前回のだとメモリ使用量がO(N)だったが、今回はO(1)
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    left_brackets = 0
    
    for s in S:
        if s == "(":
            left_brackets += 1
        else:
            if left_brackets == 0:
                return 0
            else:
                left_brackets -= 1
    
    if left_brackets == 0:
        return 1
    else:
        return 0