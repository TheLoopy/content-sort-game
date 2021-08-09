import time

def print_start_message():
	message_text1 = '\t\t\t\t   HELLO!'
	message_text2 = '\n\nContent Sort Puzzle is a fun and addictive puzzle game! Try to sort the content in the falsks until all content with the same color stay in the same flask.\n\n\nHOW TO PLAY:\n\n- Enter a flask number to move the content lie on top in the flask to another\n\n- The rule is that flask you want ot move into must has enough space\n\n- Try not to get stuck - but don\'t worry, you can always restart the level at any time\n\n- For restart enter "r"!'

	for i in message_text1:
		print(i, end='', flush=True)
		time.sleep(0.1)
	time.sleep(0.5)
	print(message_text2)
	input('\n\n\nPress "Enter" to continue...')


def print_win():
	text = ['Y','O','U','','W','I','N','!','','','','','']*4
	while True:
		print('\n'*10)
		print('-'*80)
		text.append(text.pop(0))
		print(*text)
		print()
		print('-'*80)
		print('\n\n\n\n\n\nFor new game press "Ctrl" + "c"')
		time.sleep(0.1)