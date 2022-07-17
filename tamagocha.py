from termcolor import cprint

PLUS_HELTH = 10
PLUS_HUNGRY = 10
PLUS_FAT = 10
PLUS_MOOD = 10
MIN_PLUS_HELTH = 1
MIN_PLUS_HUNGRY = 1
MIN_PLUS_FAT = 1
MIN_PLUS_MOOD = 1


class Tamagocha:

	def __init__(self, name: str, helth: int, hungry: int, fat: int, mood: int):
		if type(name) == str and type(helth) == int and type(hungry) == int and type(fat) == int and type(mood) == int:
			self.name = name
			self.helth = helth
			self.hungry = hungry
			self.fat = fat
			self.mood = mood
		else:
			cprint('TypeError: name = str, helth = int, hungry = int, fat = int, mood = int', 'red')

	def __str__(self):
		return 99*'#' + '\n' + 44*'#' + ' tamagocha ' + 44*'#' + '\n' + 99*'#' + '\n' + \
		f'Name: ' + '[' + self.name + ']' + ' ' + (99-len('Name: ')-len(self.name)-3)*'#' + '\n' + \
		99*'#' + '\n' + 'Helth:  ' + (self.helth//10)*'[+]' + ' ' + (99-len('Helth:  ')-(3*self.helth//10)-1)*'#' + '\n' + 99*'#' + '\n' + \
		'Hungry: ' + (self.hungry//10)*'[+]' + ' ' + (99-len('Hungry: ')-(3*self.hungry//10)-1)*'#' + '\n' + 99*'#' + '\n' + \
		'Sleep:  ' + (self.fat//10)*'[+]' + ' ' + (99-len('Sleep:   ')-(3*self.fat//10)-1)*'#' + '\n' + 99*'#' + '\n' + \
		'Mood:   ' + (self.mood//10)*'[+]' + ' ' + (99-len('Mood:   ')-(3*self.mood//10)-1)*'#' + '\n' + 99*'#' + '\n' + \
		'What do you want to do? ' + (99-len('What do you want to do? '))*'#' + '\n' + 99*'#' + '\n' \
		'1 - Eat ' + (99-len('1 - Eat '))*'#' + '\n' + 99*'#' + '\n' + \
		'2 - Sleep ' + (99-len('2 - Sleep '))*'#' + '\n' + 99*'#' + '\n' + \
		'3 - Play ' + (99-len('3 - Play '))*'#' + '\n' + 99*'#' + '\n' + \
		'4 - Exit ' + (99-len('4 - Exit '))*'#' + '\n' + 99*'#' + '\n'

	def rm_helth(self):
		if self.helth - PLUS_HELTH <= 0:
			cprint('Your tamagocha is dead', 'red')
			exit()
		else:
			self.helth -= PLUS_HELTH

	def rm_mood(self):
		if self.mood - PLUS_MOOD <= 0:
			self.mood = 0
			self.rm_helth()
		else:
			self.mood -= PLUS_MOOD

	def rm_min_mood(self):
		if self.mood - MIN_PLUS_MOOD <= 0:
			self.mood = 0
			self.rm_helth()
		else:
			self.mood -= MIN_PLUS_MOOD

	def add_mood(self):
		if self.mood + PLUS_MOOD >= 100:
			self.mood = 100
		else:
			self.mood += PLUS_MOOD

	def add_min_mood(self):
		if self.mood + MIN_PLUS_MOOD >= 100:
			self.mood = 100
		else:
			self.mood += MIN_PLUS_MOOD

	def rm_eat(self):
		if self.hungry - PLUS_HUNGRY <= 0:
			self.hungry = 0
			self.rm_helth()
		else:
			self.hungry -= PLUS_HUNGRY

	def rm_fat(self):
		if self.fat - PLUS_FAT <= 0:
			self.fat = 0
			self.rm_helth()
		else:
			self.fat -= PLUS_FAT

	def add_min_helth(self):
		if self.helth + MIN_PLUS_HELTH >= 100:
			self.helth = 100
		else:
			self.helth += MIN_PLUS_HELTH

	def add_eat(self):
		if self.hungry + PLUS_HUNGRY >= 100:
			self.hungry = 100
			self.rm_mood()
		else:
			self.hungry += PLUS_HUNGRY
			self.rm_min_mood()

	def add_fat(self):
		if self.fat + PLUS_FAT >= 100:
			self.fat = 100
			self.rm_mood()
		else:
			self.fat += PLUS_FAT
			self.rm_min_mood()

	def eat(self):
		self.add_eat()
		self.rm_fat()
		self.add_min_helth()

	def sleep(self):
		self.add_fat()
		self.rm_eat()
		self.add_min_helth()

	def play(self):
		self.rm_eat()
		self.rm_fat()
		self.add_mood()

