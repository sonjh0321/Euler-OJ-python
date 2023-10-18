"""
첫 줄이 홀수이면서 둘쨋 줄이 짝수이어야 공격을 피할 수 있다.
"""
first_day = int(input())
second_day = int(input())
print(1 if first_day % 2 == 0 or second_day % 2 == 1 else 0)
