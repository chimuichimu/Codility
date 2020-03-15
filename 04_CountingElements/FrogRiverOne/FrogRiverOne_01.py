# スコア100% Pythonで初のCodility
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    
    # The array to store flags
    exist_leaf = [0] * X

    # Let leaves fall as time passes
    cnt = 0
    ans = -1
    time = 0
    for leaf_position in A:
        
        if exist_leaf[leaf_position-1] == 0:
            exist_leaf[leaf_position-1] = 1
            cnt += 1
        
        if cnt == X:
            ans = time
            break

        time += 1

    return ans