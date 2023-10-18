"""
n미만 정수 중 3의 배수 합 + n 미만 정수 중 5의 배수 합 - n 미만 정수 중 15의 배수 합
"""
n = int(input())


def sum_of_multiples(n, multiple):
    # 주어진 배수의 개수를 구함
    count = (n - 1) // multiple
    # 등차수열의 합 공식 사용: (first + last) * count / 2
    return multiple * count * (count + 1) // 2


print(sum_of_multiples(n, 3) + sum_of_multiples(n, 5) - sum_of_multiples(n, 15))
