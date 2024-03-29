# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# Check if a number is prime
def isPrime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

# Check nth prime
def nthPrime(n):
    count = 2
    num = 3
    while count < n:
        num += 1
        if isPrime(num):
            count += 1
    return num


print("The 10,0001th prime number is", nthPrime(10001))
