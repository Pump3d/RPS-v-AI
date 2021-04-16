import sys
import time

choices = ["rock", "paper", "scissors"]

opps = {
	"rock": "paper",
	"paper": "scissors",
	"scissors": "rock"
}


def typewrite(words):
	for char in words:
		time.sleep(0.4)
		sys.stdout.write(char)
		sys.stdout.flush()


def processInput(input):
	if input.lower() in choices:
		return True
	else:
		sys.stdout.write("\n Invalid input, quitting")
		sys.stdout.flush()
		typewrite("...")
		time.sleep(0.4)
		print("\n")
		quit()


