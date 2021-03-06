# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        x.append(a)
    print()

x = []
y = []

fib(4000000)

for i in x:
    if i % 2 == 0:
        y.append(i)

print("The terms in the Fibonacci sequence, whose values do not exceed four million and are even valued, have a sum of ", sum(y))
