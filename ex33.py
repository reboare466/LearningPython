# ex33

def numarray(lastnum,step):

	i = 0
	numbers = []

#	while i < lastnum:
	for i in range(0, lastnum, 2):
		numbers.append(i)
		
		i = i + step
		print("Numbers now:", numbers)
		print("At the bottom i is %d" % i)
		
	print("The Numbers:")

	for num in numbers:
		print(num)
		
numarray(10,2)