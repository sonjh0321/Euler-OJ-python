a, b, c = map(int, input().split())

for i in ['+', '-', '*', '/']:
    if eval(f'{a}{i}{b}') == c:
        print(f'{a}{i}{b}={c}')
        break
    elif eval(f'{b}{i}{c}') == a:
        print(f'{a}={b}{i}{c}')
        break
