# coded and explained by DarkC343

# lists are mutable
def main():
	l = [1, 2, 3, 4]

	print(l)

	# append (add new value at end)
	l.append(9)

	# insert (add new value at specific index). method is defined in insert(index, value)
	l.insert(2, 8)

	for i in l:
		print(i)

if __name__ == '__main__':
	main()