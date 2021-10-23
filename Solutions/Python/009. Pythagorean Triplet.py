# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a² + b² = c²
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def triplet(c):
    for a in range(1, 1000):
        for b in range(a, 1000):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return a * b * c 

print("The product of abc is", triplet(1000))
