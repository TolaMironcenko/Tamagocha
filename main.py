from termcolor import cprint
from tamagocha import Tamagocha
from loader import Loader


def main():
	loader = Loader(n=100, start='^', end='^', interval=0.001, symbol='$', color='cyan', defsymbol='_', step=3)
	print('Hi, this is tamagocha\n')
	print('Write the name of your tamagocha:')
	name = input()
	animal = Tamagocha(name, 100, 100, 100, 100)
	print(animal)
	while True:
		do = input()
		if do == '1' or do == 'eat' or do == 'Eat':
			animal.eat()
			print(loader)
			print(animal)
		elif do == '2' or do == 'sleep' or do == 'Sleep':
			animal.sleep()
			print(loader)
			print(animal)
		elif do == '3' or do == 'play' or do == 'Play':
			animal.play()
			print(loader)
			print(animal)
		elif do == '4' or do == 'exit' or do == 'Exit':
			cprint('You are exited from tamagocha', 'green')
			exit()
		else:
			cprint("I can't do this")



if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		cprint('You are exited from tamagocha', 'green')
		exit()
	except Exception as e:
		cprint('Error: '+str(e), 'red')