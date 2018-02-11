# by limiting values to be under 50
def fibWhile():
	x = 1
	y = 1
	while y < 6766:
		print(y)
		x, y = y, x + y

# by iterating 10 times
def fibFor():
	x = 1
	y = 1
	for i in range(1, 20):
		print(y)
		x, y = y, x + y

# by indexing serie
def fibRecursion(n):
	if n == 1 or n == 0:
		return 1
	return fibRecursion(n-1) + fibRecursion(n-2)



fibWhile()
# fibFor()
# for i in range(0, 20):
# 	print(fibRecursion(i), end=', ')