# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Define range
x = range(1, 1000)

# Make a list to store range data
sums = []

# Loop through range, add to list and spit out the sum
for i in x: 
    if i % 3 == 0 or i % 5 == 0:
        sums.append(i)

# Print sum
print("The sum of all multiples of 3 or 5 below 1000 is...", sum(sums))


# Second solution, written as a function for taking in a user defined range
def sums_below(n):
    total = []
    for numbers in range(1, n):
        if numbers % 3 == 0 or numbers % 5 == 0:
            total.append(numbers)
    return sum(total)
        

print(sums_below(1000))
