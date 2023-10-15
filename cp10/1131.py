"""
이 문제는 시간을 더하는 문제이다.
이때, 분이 60을 초과하면 시를 올리고, 시가 24를 초과하면 0으로 돌려야 하는 것을 고려해야 한다.
"""
h, m = map(int, input().split())
td = int(input())

# 분이 올림되어서 시를 건드리게 된다면
if m+td >= 60:
    h = h + ((m+td) // 60)
    m = ((m+td) % 60)
    # 시를 건드렸는데, 그 시가 24를 넘어가게 된다면
    if h >= 24:
        h = h % 24
# 만약 분이 올림되지 않는다면
else:
    m = m + td

print(h, m)