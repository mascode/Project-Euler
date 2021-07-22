# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

natural_number = range(1, 101)
sum_of_squares = []
for number in natural_number:
    sum_of_squares.append(number**2)

square_of_sum = sum(natural_number)**2

print("The difference between the sum of the squares and the sqaure of the sum for 1-100 is", square_of_sum - int(sum(sum_of_squares)))
