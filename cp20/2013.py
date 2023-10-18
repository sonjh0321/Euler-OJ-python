"""
우선 아래 부분이 k이라면 아래 부분이 k으로 같은 도미노는 모두 k+1이다.
위 부분이 0부터 k까지 진행되기 때문이다.

즉, 아래 부분이 같은 도미노의 눈의 수는 k*(k+1) + 0부터 k까지 합
이 결괏값을 하나의 식으로 정리하고, 0<=k<=n의 범위에서의 합을 구하면 된다.
"""
n = int(input())
print(n*(n+1)*(n+2)//2)