class objectActions:
	def nationality(self): return self._selectAction('nationality')
	def religion(self): return self._selectAction('religion')
	def age(self): return self._selectAction('age')
	def name(self): return self._selectAction('name')

	def _selectAction(self, action):
		if action in self.strings:
			return self.strings[action]
		else:
			return "{} has no {}".format(self.className(), action)

	def className(self): return self.__class__.__name__.lower()

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
			name = "It is Apple Iphone 6s Plus",
			age = "About 1 year and half"
		)

class forest(objectActions):
	strings = dict(
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