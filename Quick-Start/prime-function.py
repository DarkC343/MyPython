def isPrime(n):
	if n == 1:
		print("1 is special number")
		return False

	for x in range(2, n):
		if n % x == 0:
			print(n, "is not prime: {} x {}".format(x, n // x))
			return False
	print(n, "is prime")
	return True

for m in range(1, 100):
	isPrime(m)