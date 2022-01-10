"""
File: weather_master.py
Name: Oscar Tsai
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

# This constant controls when to stop
EXIT = -100
STANDARD = 16

def main():
	"""
	TODO:
	"""
	total = 0
	print('StandCode \"Weather Master 4.0”!')
	data = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))
	if data == EXIT:
		print('No temperatures were entered.')
	else:
		maximum = data
		mini = data
		while True:
			data = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))
			if data == EXIT:
				break
			if data > maximum:
				maximum = data
			if data < mini:
				mini = data
			if data < STANDARD:
				STANDARD = data
				total += 1
		print("Highest temperature = "+str(maximum))
		print("Lowest temperature = "+str(mini))
		average = (maximum + mini) / 2
		print("Average = "+str(average))
		print(str(total)+' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
