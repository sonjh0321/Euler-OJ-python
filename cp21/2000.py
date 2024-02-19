"""
1 이상, 10 이하의 정수만 사용해야 한다는 것에 주의하면, 3중 반복문으로 해결할 수 있음.
"""
세_수의_합 = int(input())

counter = 0
if 세_수의_합 > 10:
    range_counter = 11
else:
    range_counter = 세_수의_합

for i in range(1, range_counter):
    for j in range(i+1, range_counter):
        for h in range(j+1, range_counter):
            if i+j+h == 세_수의_합:
                counter += 1
                print(f"{i} {j} {h}")
print(counter)
