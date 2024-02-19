"""
무게추가 최소 1번 이상 사용되어야 한다는 것만 주의하면 됨
"""
wight = int(input())
counter = 0
for i in range(1, 11):
    for j in range(1, 11):
        for h in range(1, 11):
            if i*2 + j*3 + h*5 == wight:
                print(f"{i} {j} {h}")
                counter += 1
print(counter)
