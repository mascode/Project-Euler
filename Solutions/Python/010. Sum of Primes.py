# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
import timeit
# Check if a number is prime
def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

# Add all the prime numbers below a given number
def sumPrimes(n):
    primes = 0
    for i in range(2, n):
        if isPrime(i):
            primes += i
    return primes

#print(sumPrimes(2000000))

# Timing the code
print(timeit.timeit("sumPrimes(2000000)", number=1, setup="from __main__ import sumPrimes"))
