# coded and explained by DarkC343

# dictionaries are mutable
'''
mutable:
	- can change (edit) entry.
	- can set a new value. (supporting +=, -=, =)
	- the id remains the same while editing. on the other hand, but it is changed when you set a value
	- two different mutable variables with the same value has different ids
'''
def main():
	a = {
		# key: value
		'name': 'C343',
		'university': 'Shahed',
		'speaking': 'Persian',
		'likes': 'programming'
	}

	print(a)
	
	print(a['name'])
	
	# inserting item to dictionary can be done using dictionay_name['key'] = value
	a['country'] = 'Iran'

	# loops display items not in defined order nor alphabeticly (scrambled)
	for i in a:
		print(i, a[i])

	# SOLUTION: sorting alphabeticly a dictionary is done with sorted() function
	# keys() method to sort keys
	for i in sorted(a.keys()):
		print(i, a[i])

	b = dict(
		# key = value
		one = 1,
		two = 2,
		three = 'se',
		four = 'four',
		five = 'panj',
	)

	print(b)

if __name__ == '__main__':
	main()