# Score 100%
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    
    dna = {"A":1, "C":2, "G":3, "T":4}
    cnt_acgt = [0,0,0,0]
    cnt_acgt_each_step = []
    answer = []

    # Count A, C, G and T at each step
    for s in S:
        if s == "A":
            cnt_acgt[0] += 1
        elif s == "C":
            cnt_acgt[1] += 1
        elif s == "G":
            cnt_acgt[2] += 1
        else:
            cnt_acgt[3] += 1
        cnt_acgt_each_step.append(cnt_acgt.copy())
    
    for p, q in zip(P, Q):
        left = cnt_acgt_each_step[p]
        right = cnt_acgt_each_step[q]
        
        minimal_impact_factor = 4
        
        if left[0] < right[0]:
            minimal_impact_factor = 1
        elif left[1] < right[1]:
            minimal_impact_factor = 2
        elif left[2] < right[2]:
            minimal_impact_factor = 3
        elif left[3] < right[3]:
            minimal_impact_factor = 4
        minimal_impact_factor = min(minimal_impact_factor, dna[S[p]])
        
        answer.append(minimal_impact_factor)    
    
    return answer