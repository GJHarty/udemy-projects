# This function will be used to find pi to the nth digit

import math

def pi_to_digit():

	while True:

		try:
			digit = int(input("Please enter a number to generate pi with that many digits. "))
			print(math.pi[:digit])

		except:
			print("Please enter an integer.")

if __name__ == '__main__':
	pi_to_digit()





