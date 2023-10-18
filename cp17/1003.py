"""
n의 짝수의 합을 구하고, 그것과 전체 합과의 차이가 홀수의 합이다.
우선 짝수의 개수의 최대는 n // 2이다.
이것을 이용해 2k에서 1<=k<=n//2 범위를 적용해 합을 구하면 짝수의 합이다.
"""
n = int(input())
even = n // 2
total = n*(n+1)//2
even_total = even * (even + 1)
print(even_total)
print(total-even_total)
