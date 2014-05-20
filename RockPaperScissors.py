print "Enter 1 for Rock, 2 for Paper, or 3 for Scissors"
userMove = input("What is your move?" + '\n')

if userMove == 1 :
	userMove = "rock"
if userMove == 2 :
	userMove = "paper"
if userMove == 3 :
	userMove = "scissors"

print '\n' + "You choose:", userMove


import random
compMove = random.randint(1,3)

if compMove == 1 :
	compMove = "rock"
if compMove == 2 :
	compMove = "paper"
if compMove == 3 :
	compMove = "scissors"

print "Opponent chooses: " + (compMove)


if userMove == compMove :
	print "This is a TIE!"
	
elif userMove == "rock" + compMove == "paper" :
	print "You LOSE!"

elif userMove == "rock" + compMove == "scissors" :
	print "You WIN!"
	
elif userMove == "paper" + compMove == "rock" :
	print "You WIN!"
	