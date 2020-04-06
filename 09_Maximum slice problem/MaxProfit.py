# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    
    if len(A) == 0:
        return 0
    
    max_price = [0] * len(A)
    min_price = [0] * len(A)
    max_profit = 0
    
    min_price[0] = A[0]
    for i in range(1,len(A)):
        min_price[i] = min(min_price[i-1],A[i])
    
    max_price[len(A)-1] = A[len(A)-1]
    for i in range(2,len(A)+1):
        max_price[len(A)-i]=max(max_price[len(A)-i+1],A[len(A)-i])
    
    for i in range(0,len(A)-1):
        tmp = max_price[i+1] - min_price[i]
        max_profit = max(max_profit,tmp)
    
    return max_profit