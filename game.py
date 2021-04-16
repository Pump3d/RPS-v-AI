from random import choices as rnd
import rpsglobals
import sys
import time

weights = [0.33, 0.33, 0.33]
scores = {
	"ai": 0,
	"ply": 0
}

def aiChoose(plyChoice):
	sys.stdout.write("\n The AI is choosing, please wait")
	sys.stdout.flush()
	rpsglobals.typewrite("...")
	time.sleep(0.4)
	sys.stdout.flush()
	
	aiChoice = rnd(
		rpsglobals.choices,
		weights=weights,
		k=1
	)
	aiChoice = aiChoice[0]

	if plyChoice == aiChoice:
		weights[rpsglobals.choices.index(rpsglobals.opps[plyChoice])]
		sys.stdout.write("\r The AI chooses " + aiChoice + "! The score remains the same. (" + str(scores["ai"]) + " - " + str(scores["ply"]) + ")")
		sys.stdout.flush()
	elif plyChoice != rpsglobals.opps[aiChoice]:
		scores["ai"] += 1
		sys.stdout.write("\r The AI chooses " + aiChoice + "! The AI has gained 1 point. (" + str(scores["ai"]) + " - " + str(scores["ply"]) + ")")
		sys.stdout.flush()
	else:
		scores["ply"] += 1
		sys.stdout.write("\r The AI chooses " + aiChoice + "! You have gained 1 point. (" + str(scores["ai"]) + " - " + str(scores["ply"]) + ")")
		sys.stdout.flush()

		for x in range(0, len(weights)):
			if x == rpsglobals.choices.index(rpsglobals.opps[plyChoice]):
				weights[x] += 0.1
			else:
				if weights[x] <= 0:
					continue
	
				weights[x] -= 0.05
	
		print(weights)

	time.sleep(0.5)
	ans = input("\n \n  > ")
	ans = ans.lower()
	if rpsglobals.processInput(ans):
		aiChoose(ans)