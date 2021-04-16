from random import choices as rnd
import rpsglobals
import sys
import time

weights = [0.33, 0.33, 0.33]

def aiChoose(plyChoice):
	sys.stdout.write("\n The AI is choosing, please wait")
	sys.stdout.flush()
	rpsglobals.typewrite("...")
	time.sleep(0.4)
	print("\n")

	aiChoice = rnd(
		rpsglobals.choices,
		weights=weights,
		k=20
	)
	print(aiChoice)