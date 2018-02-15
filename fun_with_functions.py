# function for printing even and odd numbers from 1 to num
def odd_even(num):
	for x in range(1, num+1):
		if x % 2 == 0:
			print "Number is " + str(x) + ". This is an even number."
		else:
			print "Number is " + str(x) + ". This is an odd number."

# takes a list and multiplies each item by num
def multiply(l, num = 5):
	for x in range(len(l)):
		l[x] *= num
	return l


# hacker challenge
def layered_multiples(arr):
	new_array = []
	for x in arr:
		temp = []
		for y in range(x):
			temp.append(1)
		new_array.append(temp)

	return new_array


odd_even(2000)

a = [2,4,10,16]
b = multiply(a, 5)
print b

c = layered_multiples(multiply([2,4,5], 3))
print c