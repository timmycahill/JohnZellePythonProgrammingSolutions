# shuffle.py

from random import randrange

def shuffle(myList):
	for i in range(len(myList) * 10):
		i1 = randrange(0, len(myList))
		i2 = randrange(0, len(myList))
		myList[i1], myList[i2] = myList[i2], myList[i1]

def main():
	myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	print(myList)
	shuffle(myList)
	print(myList)

if __name__ == '__main__':
	main()