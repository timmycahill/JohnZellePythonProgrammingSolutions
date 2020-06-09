# stats.py

from math import sqrt

def getNumbers():
	nums = [] 		# start with an empty list

	# sentinel loop to get numbers
	xStr = input("Enter a number (<Enter> to quit) >> ")
	while xStr != "":
		x = eval(xStr)
		nums.append(x)		# add this value to the list
		xStr = input("Enter a number (<Enter> to quit) >> ")
	return nums

def mean(nums):
	sum = 0.0
	for num in nums:
		sum = sum + num
	return sum / len(nums)

def stdDev(nums):
	sumDevSq = 0.0
	xbar = mean(nums)
	for num in nums:
		dev = num - xbar
		sumDevSq = sumDevSq + dev * dev
	return sqrt(sumDevSq/(len(nums)-1))

def median(nums):
	nums.sort()
	size = len(nums)
	midPos = size // 2
	if size % 2 == 0:
		median = (nums[midPos] + nums[midPos-1]) / 2.0
	else:
		median = nums[midPos]
	return median

def meanStdDev(nums):
	sumDevSq = 0.0
	xbar = mean(nums)
	for num in nums:
		dev = num - xbar
		sumDevSq = sumDevSq + dev * dev
	std = sqrt(sumDevSq/(len(nums)-1))
	return xbar, std

def main():
	print("This program computes mean, median and standard deviation.")

	data = getNumbers()
	xbar = mean(data)
	std = stdDev(data)

	print("\nThe mean is", xbar)
	print("The standard deviation is", std)
	xbar, std = meanStdDev(data)
	print("The mean is {0} and the standard deviation is {1}.".format(xbar, std))

if __name__ == '__main__': main()
