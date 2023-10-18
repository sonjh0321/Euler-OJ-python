def sum_of_divisors(n):
    divisors = [1]  # 1은 모든 자연수의 약수입니다.
    if n > 1:
        divisors.append(n)  # n 자신도 약수입니다. (1의 경우 제외)

    for i in range(2, int(n ** 0.5) + 1):  # n의 제곱근까지만 확인
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # 제곱근이 아닐 경우 짝을 이루는 약수도 추가
                divisors.append(n // i)

    return sum(divisors)


n = int(input())
print(sum_of_divisors(n))
