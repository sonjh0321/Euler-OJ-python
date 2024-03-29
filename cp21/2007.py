"""
1       1
12     21
123   321
1234 4321
123454321
1234 4321
123   321
12     21
1       1

우선 나비를 3가지로 분류해야 한다.
- 위쪽 부분
- 가운데 줄
- 아래쪽 부분

위쪽 부분과 아래쪽 부분은 다시 3가지로 분류할 수 있다.
- 왼쪽
- 가운데 공백
- 오른쪽

우선 위쪽의 왼쪽을 살펴보겠다.
위쪽의 왼쪽은 매우 간단하다. 왼쪽의 높이는 1부터 (나비 크기 - 1)까지 반복하는 것과 같다. 즉, 나비 크기 - 1이다.
각 줄은 1부터 현재 높이(첫 번째 줄을 1층으로 간주할 때)까지 반복하는 것과 같다.

이제 위쪽의 가운데 공백을 살펴보아야 한다.
공백은 나비의 넓이를 이용해야 한다. 왼쪽과 오른쪽의 숫자들의 개수와 공백을 더한 값은 항상 나비의 넓이와 일치해야 한다.
즉, 나비의 넓이(나비의 크기 * 2 - 1) - 왼쪽에서 사용한 문자의 개수 * 2이다.

이제 위쪽의 오른쪽을 살펴보아야 한다.
오른쪽은 역순으로 출력되기에 유의해야 한다.
현재 층에서 왼쪽에 있는 값을 빼고 1을 더하면 역순으로 출력한 것과 동일하다.
왜냐하면 현재층수 == 정방향 출력의 마지막이기 때문이다.
    예를 들어 123은 3층에서 출력되는 값들이다. 123의 마지막인 3은 현재 층과 동일하다. 이를 이용하는 것이다.

나비의 가운데는 우선 나비의 크기 * 2에서 하나 작은 값만큼을 출력한다.
만약 출력하면서 나비의 크기보다 큰 값은 나비의 크기*2에서 값을 빼주면 된다.
    예를 들어 123456789의 경우 6부터 9까지는 10에서 빼주면 된다.
    이들은 (나비의 크기 + 위치(1..4))와 동일하므로 나비의 크기 * 2 - 나비의 크기 - 위치 == 나비의 크기 - 위치
    즉, 위치 값은 갈수록 늘어나므로, 결론적으로 값이 다시 작아지는 대칭 형태가 나타나게 된다.

나비의 아래쪽은 위쪽에서의 출력을 반대로 하면 된다.
반복문의 시작과 끝을 뒤집고, 반복 방향을 -1로 하면 된다.
"""
size = int(input())

for i in range(1, size):
    for j in range(1, i+1):
        print(j, end='')

    print(' '*(size*2-1 - i*2), end='')

    for j in range(1, i+1):
        print(i+1-j, end='')

    print()

for i in range(1, size*2):
    if i > size:
        print(2*size-i, end='')
        continue
    if i == 10:
        print('0', end='')
        continue
    print(i, end='')
print()

for i in range(size-1, 0, -1):
    for j in range(i, 0, -1):
        print(i+1-j, end='')

    print(' '*(size*2-1 - i*2), end='')

    for j in range(i, 0, -1):
        print(j, end='')
    print()