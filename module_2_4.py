
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for x in numbers:
    if x > 1:
        for i in range(2, x // 2):
            if (x % i) == 0:
                break
        else:
            primes.append(x)
    else:
        not_primes.append(x)
print("Простые числа:", primes)
print("Непростые числа:", not_primes)