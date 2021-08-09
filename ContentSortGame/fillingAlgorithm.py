from random import randint, sample
fillers = ['░', '▓', '█']


def fill(flasks):
	numbers = '123'*3
	mixed_numbers = ''.join(sample(numbers, len(numbers)))

	random_filling = random_amount()
	numbers_in_flasks = (mixed_numbers[:random_filling[0]], mixed_numbers[random_filling[0]:random_filling[0]+random_filling[1]], mixed_numbers[random_filling[0]+random_filling[1]:])

	for i in range(3):
		for j in numbers_in_flasks[i]:
			flasks[i].append(fillers[int(j)-1])			


def get_count(count):
	if count >= 4:
		return 4
	return count


def random_in_flask(flask_amount, count):
	if get_count(count) > 5-flask_amount:
		return randint(0, 5-flask_amount)
	return randint(0, get_count(count))


def random_amount():
	count = 9
	flask_amount_1, flask_amount_2, flask_amount_3 = 0, 0, 0
	while count > 0:
		random_f1 = random_in_flask(flask_amount_1, count)
		flask_amount_1 += random_f1
		count -= random_f1

		random_f2 = random_in_flask(flask_amount_2, count)
		flask_amount_2 += random_f2
		count -= random_f2

		random_f3 = random_in_flask(flask_amount_3, count)
		flask_amount_3 += random_f3
		count -= random_f3 

	return (flask_amount_1, flask_amount_2, flask_amount_3)