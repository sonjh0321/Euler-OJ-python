"""
2를 제외한 모든 짝수는 다른 짝수들의 합으로 표현할 수 있다.
"""
w = int(input())
print("NO" if w % 2 != 0 else "NO" if w == 2 else "YES")
