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

def main():
	"""
	TODO:
	"""
	print('StandCode \"Weather Master 4.0”!')
	data = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))
	if data == EXIT:
		print('No temperatures were entered.')
	else:
		maximum = data
		min = data
		standard = 16
		total = 0
		while True:
			data = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))
			if data == EXIT:
				break
			if data > maximum:
				maximum = data
			if data < min:
				min = data
			if data < standard:
				total += 1
		print("Highest temperature = "+str(maximum))
		print("Lowest temperature = "+str(min))
		average = (maximum + min) / 2
		print("Average = "+str(average))
		print(str(total)+' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
