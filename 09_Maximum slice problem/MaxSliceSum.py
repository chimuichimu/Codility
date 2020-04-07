# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    max_end = -1000000
    max_slice = -1000000
    
    for elm in A:
        max_end = max(elm, max_end + elm)
        max_slice = max(max_slice, max_end)
    
    return max_slice