# innerProd.py

def innerProd(x, y):
	prod = 0
	for i in range(len(x)):
		prod += x[i] * y[i]
	return prod

def main():
	list1 = []
	list2 = []

	value = input("Enter a value for the first list: ")
	while value != "":
		list1.append(eval(value))
		value = input("Enter a value for the first list: ")

	for i in range(len(list1)):
		value = eval(input("Enter a value for the second list: "))
		list2.append(value)

	print(list1)
	print(list2)

	print("The inner product is", innerProd(list1, list2))

if __name__ == '__main__':
	main()