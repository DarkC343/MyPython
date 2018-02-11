def isPrime(n):
	if n == 1:
		return False

	for x in range(2, n):
		if n % x == 0:
			return False

	return True


def primeGenerator(n = 1):
	while True:
		if isPrime(n):
			yield n
		n += 1

for n in primeGenerator():
	if n > 1000: break
	print(n)