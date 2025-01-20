def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def quality_control_primes(max_items):
    prime_positions = []
    for item in range(1, max_items + 1):
        if is_prime(item):
            prime_positions.append(item)
    return prime_positions

max_items = 1000
prime_items = quality_control_primes(max_items)


print(f"Items that need extra quality control (prime-numbered positions): {prime_items}")