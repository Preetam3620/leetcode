class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        primes = [True] * n
        primes[0], primes[1] = False, False

        for num in range(2, int(n**0.5) + 1):
            if primes[num]:
                for i in range(num*num, n, num):
                    primes[i] = False

        # counts = Counter(primes)
        return sum(primes)