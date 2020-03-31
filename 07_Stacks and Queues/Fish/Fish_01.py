# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    survivals = 0
    stack = []
     
    for idx in range(0,len(A)):
        if B[idx] == 0:
            while len(stack) != 0:
                if stack[-1] > A[idx]:
                    break
                else:
                    stack.pop()
                         
            else:
                survivals += 1
        else:
            stack.append(A[idx])
             
    survivals += len(stack)
     
    return survivals