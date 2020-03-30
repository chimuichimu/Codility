# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    
    # リストが空かチェック
    N = len(S)
    if N == 0:
        return 1
    
    # ネストのリスト作成
    nests = ["()", "{}", "[]"]
    
    # 評価用のスタック準備
    stack = []
    
    # Sの各要素に対して、スタックがゼロか、スタックの末尾と組み合わせたときにネストが完成していたら
    # スタックの末尾を削除 そうでなければ要素をスタックにアペンド
    # 最終的に残ったスタックの要素数がゼロならばproperly nested
    for i in range(0, N):
        if len(stack) == 0 or stack[-1] + S[i] not in nests:
            stack.append(S[i])
        else:
            stack.pop()
    if len(stack) == 0:
        return 1
    else:
        return 0