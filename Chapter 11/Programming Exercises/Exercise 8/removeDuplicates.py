# removeDuplicates.py

def removeDuplicates(someList):
	listTracker = []
	i = 0
	while i < len(someList):
		if someList[i] in listTracker:
			del someList[i]
		else:
			listTracker.append(someList[i])
			i += 1

def main():
	someList = []
	value = input("Enter a value: ")
	while value != "":
		someList.append(value)
		value = input("Enter a value: ")

	print(someList)
	removeDuplicates(someList)
	print(someList)

if __name__ == '__main__':
	main()