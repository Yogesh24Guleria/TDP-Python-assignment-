n = int(input("Enter number of terms:"))
a = 0
b = 1
sum = 0

for i in range(n):
	print(sum, end=" ")
	sum = a+b
	b = a
	a = sum