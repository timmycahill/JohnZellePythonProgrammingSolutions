# sieveAlgorithm.py

def sieve(n):
	numbers = []
	for i in range(2, n):
		numbers.append(i)

	primes = []
	while len(numbers) != 0:
		i = 0
		value = numbers[i]
		primes.append(value)
		while i < len(numbers):
			if numbers[i] % value == 0:
				del numbers[i]
			else:
				i += 1
	return primes

def main():
	printIntroduction()
	n = getInputs()
	primes = sieve(n)
	outputResults(primes)

def printIntroduction():
	print("This program returns the prime numbers up to a given number using " +
		"Sieve's algorithm.\n")

def getInputs():
	return int(input("Enter a value to go up to: "))

def outputResults(primes):
	print(primes)

if __name__ == '__main__':
	main()