try:
	fh = open('sometext.txt')

	for line in fh.readlines():
		print(line, end='')
except IOError as e:
	print("Error: {}".format(e))

print("After error handling")