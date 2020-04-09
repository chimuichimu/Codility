# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    peaks = [] # Position of flag candidates
    
    # Calculate positions of flag candiates
    for idx in range(1,len(A)-1):
        if A[idx] > A[idx-1] and A[idx] > A[idx+1]:
            peaks.append(idx)
    
    # Calculate the number of flags
    for flag_number in reversed(range(0,len(peaks)))):
        for peak in peaks:
            