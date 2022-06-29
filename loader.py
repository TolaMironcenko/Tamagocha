from termcolor import cprint
import time


class Loader:
	def __init__(
		self, 
		n: int = 100, 
		start: str = '|', 
		end: str = '|', 
		interval: float = 0.1, 
		color: str = 'green', 
		symbol: str = '█', 
		step: int = 1, 
		display: str = 'percent',
		defsymbol: str = '.'
	):
		self.n = n
		self.start = start
		self.end = end
		self.interval = interval
		self.color = color
		self.symbol = symbol
		self.step = step
		self.display = display
		self.defsymbol = defsymbol

	def __str__(self):
		for percent in range(self.n+1):
			s = self.start+f"{(percent // self.step) * self.symbol}"
			s += f"{(self.n//self.step - (percent // self.step)) * self.defsymbol}" + self.end + ' '
			s += f"{percent}"
			if self.display == 'percent':
				s+='%'
			elif self.display == 'of':
				s+=f'/{self.n}'
			cprint(s, self.color, end="\r")
			time.sleep(self.interval)
		return s