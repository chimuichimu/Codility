# Score100% 計算複雑性はO(N*Log(N) or O(N))
# 円の左端と右端にそれぞれ+1, -1とタグ付けし、ソートする
# ソートした配列を小さい順から見ていき、生きている円（active_circles）をカウントしながら
# 円の重なりの数（intersections）をカウントする
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    events = []
    for i, a in enumerate(A):
        events += [(i-a, +1), (i+a, -1)]
    events.sort(key=lambda x: (x[0], -x[1]))

    intersections, active_circles = 0, 0
    for _, circle_count_delta in events:
        intersections += active_circles * (circle_count_delta > 0)
        active_circles += circle_count_delta
        if intersections > 10E6:
            return -1
    return intersections