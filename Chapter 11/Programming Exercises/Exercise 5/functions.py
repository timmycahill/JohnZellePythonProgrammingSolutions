# functions.py

def count(myList, x):
	count = 0
	for item in myList:
		if item == x:
			count += 1
	return count

def isin(myList, x):
	for item in myList:
		if item == x:
			return True
	return False

def index(myList, x):
	for i in range(len(myList)):
		if myList[i] == x:
			return i
	return -1

def reverse(myList):
	for i in range(len(myList) // 2):
		myList[i], myList[-(i + 1)] = myList[-(i + 1)], myList[i]

def sort(myList):
	for i in range(1, len(myList)):
		key = myList[i]
		j = i - 1
		while j >= 0 and key < myList[j]:
			myList[j + 1] = myList[j]
			j -= 1
		myList[j + 1] = key



def main():
	myList = [1,2,3,4,5,6,7,8,9]
	print(myList)
	reverse(myList)
	print(myList)
	sort(myList)
	print(myList)

if __name__ == '__main__':
	main()