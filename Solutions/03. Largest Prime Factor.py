# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

def factorize():
	n = int(input("What number do you want the largest prime factor for?"))
	p = 2
	print("Your prime factors are...")
	while n >= p * p:
		if n % p == 0:
			print(p)
			n = n / p
		else: 
			p = p + 1
	print(int(n))
	print("The largest prime factor of your number is", int(n))
	
factorize()
