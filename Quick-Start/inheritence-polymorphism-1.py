class objectActions:
	def nationality(self): return self.strings['nationality']
	def religion(self): return self.strings['religion']
	def age(self): return self.strings['age']
	def name(self): return self.strings['name']

class person(objectActions):
	strings = dict(
			nationality = "I am Iranian",
			religion = "It is Islam",
			name = "My name is AmirMohammad",
			age = "I am 18"
		)

class cellphone(objectActions):
	strings = dict(
			nationality = "It is made in China but from USA",
			religion = "No religion is defined for cellphones!",
			name = "It is Apple Iphone 6s Plus",
			age = "About 1 year and half"
		)

class forest(objectActions):
	strings = dict(
			nationality = "No nationality is defined for forest!",
			religion = "No nationality is defined for forest!",
			name = "No name is defined for forest",
			age = "It is about the world age"
		)

def displayActions(object):
	print(object.nationality())
	print(object.religion())
	print(object.name())
	print(object.age())


def main():
	mamad = person()
	iphone = cellphone()
	jungles = forest()

	for i in ( mamad, iphone, jungles ):
		displayActions(i)

if __name__ == '__main__':
	main()