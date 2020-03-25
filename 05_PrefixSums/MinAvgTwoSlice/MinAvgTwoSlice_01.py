# Score60% ロジックミス
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # n個の集合（n>3）に対して、この集合が最小の平均値を持つと仮定する。
    # このとき集合を２つのブロックに分けると、それぞれのブロックの平均値は、
    # 元の集合と同じ平均値をとるか、元の集合より大きい値と小さい値をとる。
    # これは「最小の平均値を持つ」という仮定に反する。
    # 以上から最小の平均値を持つブロックの要素数は、２つor３つであるといえる。
    # 従って、以下のロジックでは2個あるいは3個の組み合わせについて、最小のものを探す。
    
    # 初期化
    min_ave = (A[0] + A[1]) / 2
    min_index = 0
    
    if len(A) == 2:
        return 0

    for i in range(2, len(A)-1):
        twins_ave = (A[i] + A[i-1]) / 2
        trips_ave = (A[i] + A[i-1] + A[i-2]) / 3
        
        if twins_ave < min_ave:
            min_ave = twins_ave
            min_index = i-1
        
        if trips_ave < min_ave:
            min_ave = twins_ave
            min_index = i-2
        
    return min_index