# coded and explained by DarkC343

# strings are immutable

# important notes:
# string item cannot be assigend to a new value. (no s[1] = "a")

def main():
	s = "salam dooste man"

	print(s)

	print(s[0]) # subscripts are used as index to display specific value

	print(s[0:5]) # slice feature to display 0 element to 4th element

	print(type(s))

	for i in s:
		print(i)

	# WARNING: We cannot use this method as we used to (like c++), i is not a counter. it contains value therfore it is an iterator
	# for i in s:
	# 	print(s[i])

	h = "khoda\nhafez"
	print(h) # displays the message in two individual lines (\n makes a new line)

	p = r"khoda\nhafez"
	print(p) # displays the message in a single line (r at the beginning makes raw format)

	# multi line string can be implemented with '''
	# use \ (forward slash) to avoid first and last new line to be displayed
	m = '''\
	this is a multi line message
which indents and white spaces        r e a l l y  matters!!
 as you can see
lines and lines\
	'''

	print(m)

if __name__ == '__main__':
	main()