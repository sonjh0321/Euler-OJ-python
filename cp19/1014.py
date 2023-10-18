factorial_str = ''


def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n-1)


n = int(input())
factorial_str += f'{n}!=('
for i in range(1, n):
    factorial_str += f'{i}*'
factorial_str += f'{n})={f(n)}'
print(factorial_str)
