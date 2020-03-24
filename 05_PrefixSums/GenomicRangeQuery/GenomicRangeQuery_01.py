# Score 62% Correctnessは100%だけど、Performanceが0%
# forの二重ループにより、O(N*M)のTime Complexity
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # 戻り値
    answer = list(range(0))
    
    # DNAの辞書
    dna = {"A":1, "C":2, "G":3, "T":4}
    
    for p,q in zip(P, Q):
        minimal_impact_factor_string = "T"
        for i in range(p, q+1):
            # Aだったらループ抜ける
            if S[i] == "A":
                minimal_impact_factor_string = "A"
                break
            # 値の更新
            minimal_impact_factor_string = min(minimal_impact_factor_string, S[i])
        
        # 戻り値にアペンド
        answer.append(dna[minimal_impact_factor_string])
        
    return answer 