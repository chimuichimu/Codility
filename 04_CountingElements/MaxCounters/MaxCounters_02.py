# Score 100%　 Max counter発動時に全更新するのではなく、一旦最大値を保持しておいて、
# それを各要素を参照したときに入れておく。最後のターンが終わったときにだけ、全部の要素を見て更新する。
# どうせまた全更新するんだし、今全更新しなくてもよいよね、という発想のロジック
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    
    # define initial counters
    cnts = [0] * N
    
    # define max counter
    prev_max_cnt = 0
    curr_max_cnt = 0
    
    # let counters operate
    for a in A:
        if 1 <= a <= N:
            if prev_max_cnt > cnts[a-1]:
                cnts[a-1] = prev_max_cnt
            cnts[a-1] += 1
            curr_max_cnt = max(curr_max_cnt, cnts[a-1])
        else:
            prev_max_cnt = curr_max_cnt
    
    for index in range(0,N):
        if cnts[index] < prev_max_cnt:
            cnts[index] = prev_max_cnt
            
    return cnts