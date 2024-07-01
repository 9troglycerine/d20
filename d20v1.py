## Importing necessary modules:

from random import randint

## Defining global Variables:

result = 'null'
menu = '\nRoll a die!\n\n1  ==> Coin flip\n2  ==> d4\n3  ==> d6\n4  ==> d8\n5  ==> d10\n6  ==> d12\n7  ==> d20\n8  ==> d100\n\nm => Show this menu\na => Show additional options menu\nq => Quit \n'
addl_menu = '\nfc ==> force a critical, either a 1 or 20\ncd ==> Roll custom die\n9  ==> d20 with no 1 or 20\n10 ==> d20 with advantage\n11 ==> d20 with disadvantage\n'
crit = [1,20]
run = True
custom_die = 'null'
cd_sides = 'null'



print(menu)
while run == True:
	selection = input("Choose your die to roll => ")

	## Flipping a coin
	if selection == '1':
		coinflip = randint(0,1)
		if coinflip == 0:
			print('\nIt came up heads\n')
		else:
			print('\nIt came up tails\n')

	## Rolling a d4
	elif selection == '2':
		result = randint(1,4)
		print(f'\nYou rolled a {result}!')

	## Rolling a d6
	elif selection == '3':
		result = randint(1,6)
		print(f'\nYou rolled a {result}!')

	## Rolling a d8
	elif selection == '4':
		result = randint(1,8)
		print(f'\nYou rolled a {result}!')

	## Rolling a d10
	elif selection == '5':
		result = randint(1,10)
		print(f'\nYou rolled a {result}!')

	## Rolling a d12
	elif selection == '6':
		result = randint(1,12)
		print(f'\nYou rolled a {result}!')

	## Rolling a d20
	elif selection == '7':
		result = randint(1,20)
		if result in crit:
			print(f'\n-==|=====>CRITICAL<=====|==-\n|--~-~-~     {result}     ~-~-~---|\n-==|=====>CRITICAL<=====|==-')
		else:
			print(f'You rolled a {result}!')


	## Rolling a d100
	elif selection == '8':
		result = randint(1,100)
		print(f'\nYou rolled a {result}!')

	## Rolling a d20 without possibility of a crit
	elif selection == '9':
		result = randint(2,19)
		print(f'\nYou rolled a {result}!')

	## Rolling a d20 with advantage
	elif selection == '10':
		## Calculating advantage
		num1 = randint(1,20)
		num2 = randint(1,20)
		if num1 > num2:
			result = num1
		else:
			result = num2
		if result in crit:
			print(f'\n-==|=====>CRITICAL<=====|==-\n|--~-~-~     {result}     ~-~-~---|\n-==|=====>CRITICAL<=====|==-')
		else:
			print(f'\nYou rolled a {result}')
	## Rolling a d20 with disadvantage
	elif selection == '11':
		## Calculating advantage
		num1 = randint(1,20)
		num2 = randint(1,20)
		if num2 > num1:
			result = num1
		else:
			result = num2
		if result in crit:
			print(f'\n-==|=====>CRITICAL<=====|==-\n|--~-~-~     {result}     ~-~-~---|\n-==|=====>CRITICAL<=====|==-')
		else:
			print(f'\nYou rolled a {result}')

	## Rolling the custom die
	elif selection == 'cd':
		cd_sides = int(input('How many sides?: '))
		result = randint(1,cd_sides)
		print(f'\nYou rolled a {result}')


	## Special Settings
	elif selection == 'm':
		print(menu)

	elif selection == 'q':
		run = False

	elif selection == 'a':
		print(addl_menu)



		##  +++++++++++++++++++++++++++++++++++++++++
		##  + This section exits mainly for testing +
		##  +++++++++++++++++++++++++++++++++++++++++


	## Forcing a crit
	elif selection == 'fc':
		num = randint(0,1)
		if num == 1:
			result = 20
		else:
			result = 1
		if result in crit:
			print(f'\n-==|=====>CRITICAL<=====|==-\n|--~-~-~     {result}     ~-~-~---|\n-==|=====>CRITICAL<=====|==-')
		else:
			print(f'\nYou rolled a {result}!')


	else:
		print("\nInput not recognized\n")


