def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_twin_primes(limit):
    twin_primes = []
    for i in range(2, limit - 1):
        if is_prime(i) and is_prime(i + 2):
            twin_primes.append((i, i + 2))
    return twin_primes

limit = 100
twin_primes = find_twin_primes(limit)

print(f"Twin prime numbers less than {limit} are:")
for twin in twin_primes:
    print(twin)


print(100**0.5)