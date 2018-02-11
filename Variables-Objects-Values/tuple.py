# coded and explained by DarkC343

# tuples are immutable

'''
immutable:
	- cannot change (edit) entry.
	- can set a new value. (supporting +=, -=, =)
	- the id changes every time when you set a value
	- two different immutable variables with the same value has same ids
'''

def main():
	x = (1, 2, 3, 4, 5, 6, 7)

	print(x)

	print(type(x))

	for i in x:
		print(i)


if __name__ == '__main__':
	main()