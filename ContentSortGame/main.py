from copy import deepcopy
import time
import os
import messages
import fillingAlgorithm

os.system('mode con: cols=80 lines=20')
class Flasks():
	def __init__(self):
		self.flasks = [
				  [],
				  [],
			      []
			     ]

	def fill_flasks(self):
		fillingAlgorithm.fill(self.flasks)

	def clear_flasks(self):
		for i in self.flasks:
			i.clear()

	def check_win(self):
		foo = 0
		for i in self.flasks:
			if len(i) == 3 and 3 - i.count(i[0]) == 0:
				foo += 1
		if foo == 3:
			return True
		else:
			return False

	def swap_numbers(self):
		try:
			choose_flask1 = (input('1| Choose flask 1 [1-3]: '))
			if choose_flask1 == 'r':
				self.clear_flasks()
				self.fill_flasks()
			else:
				choose_flask1 = int(choose_flask1)
				self.print_flasks()
				choose_flask2 = (input('2| Choose flask 2 [1-3]: '))
				if choose_flask2 == 'r':
					self.clear_flasks()
					self.fill_flasks()
				else:
					choose_flask2 = int(choose_flask2)
					if choose_flask1 in range(1, 4) and choose_flask2 in range(1, 4):		
						first_chosed_flask = self.flasks[choose_flask1-1]
						second_chosed_flask = self.flasks[choose_flask2-1]

						if len(first_chosed_flask) == 0:
							print(f'\n\n\n\nFlask {choose_flask1} is empty!')
						elif len(second_chosed_flask) < 5:
							last_num = first_chosed_flask.pop(0)
							second_chosed_flask.insert(0, last_num)
						else:
							print(f'\n\n\n\nFlask {choose_flask2} is full!')
					else:
						raise ValueError
		except ValueError:
			print('\n\n\n\nInvallid input, please enter correct number!')

	def print_flasks(self):
		printed_flasks = deepcopy(self.flasks)
		one_diemnisional_list = []
		for flask in printed_flasks:
			foo = 5 - len(flask)
			for i in range(foo):
				flask.insert(0, ' ')
		for i in range(len(printed_flasks)):
			one_diemnisional_list += (list(printed_flasks[i]))
		print( '''\n\n\n\n\n
	 	\t\t_ _  _ _  _ _
	 	\t\t|{0}|  |{5}|  |{10}|
	 	\t\t|{1}|  |{6}|  |{11}|
	 	\t\t|{2}|  |{7}|  |{12}|
	 	\t\t|{3}|  |{8}|  |{13}|
	 	\t\t|{4}|  |{9}|  |{14}|
	 	\t\t -    -    -  \n\n\n\n
		'''.format(*one_diemnisional_list))

	def main_loop(self):
		self.print_flasks()
		self.swap_numbers()
		if self.check_win():
			for i in range(5):
				print('\n'*20)
				time.sleep(0.3)
				self.print_flasks()
				time.sleep(0.3)
			try:
				messages.print_win()
			except KeyboardInterrupt:
				self.clear_flasks()
				self.fill_flasks()
		self.main_loop()
	

messages.print_start_message()
game = Flasks()
game.fill_flasks()
game.main_loop()