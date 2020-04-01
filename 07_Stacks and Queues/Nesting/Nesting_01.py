# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    stack = []
    for s in S:
        stack.append(s)
        if len(stack) > 1:
            if stack[-2] + stack[-1] == "()":
                stack.pop()
                stack.pop()
    if len(stack) == 0:
        return 1
    else:
        return 0