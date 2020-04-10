# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    
    min_perimeter = 100000000000
    
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            a = i
            if i != N // i:
                b = N // i
            else:
                b = a
            min_perimeter = min(min_perimeter, 2*(a+b))
    
    return min_perimeter