import random

#wins
winner = ""
your_wins = 0
ai_wins = 0
choices = ["rock", "paper", "scissors"]

def win(winner, ai_wins, your_wins):
	if(winner == "ai"):
		print "you lost!"
		ai_wins = ai_wins + 1
		print "You %d - %d AI" % (your_wins, ai_wins)
		return ai_wins;
	elif(winner == "you"):
		print "you won!"
		your_wins = your_wins + 1
		print "You %d - %d AI" % (your_wins, ai_wins)
		return your_wins;
	elif(winner == "nobody"):
		print "draw!"
		return;
play = 1
while(play == 1):
	ai_wins = 0
	your_wins = 0
	while(ai_wins < 3 and your_wins < 3):
		your_choice = raw_input("rock, paper or scissors?: ")
		ai_choice = random.choice(choices) 
		if(your_choice == "rock"):
			if(ai_choice == "paper"):
				winner = "ai"
				ai_wins = win(winner, ai_wins, your_wins)
			elif(ai_choice == "scissors"):
				winner = "you"
				your_wins = win(winner, ai_wins, your_wins)
			elif(ai_choice == "rock"):
				winner = "nobody"
				win(winner, ai_wins, your_wins)
		elif(your_choice == "paper"):
				if(ai_choice == "paper"):
					winner = "nobody"
					win(winner, ai_wins, your_wins)
				elif(ai_choice == "scissors"):
					winner = "ai"
					ai_wins = win(winner, ai_wins, your_wins)
				elif(ai_choice == "rock"):
					winner = "you"
					your_wins = win(winner, ai_wins, your_wins)
		elif(your_choice == "scissors"):
				if(ai_choice == "paper"):
					winner = "you"
					your_wins = win(winner, ai_wins, your_wins)
				elif(ai_choice == "scissors"):
					winner = "nobody"
					win(winner, ai_wins, your_wins)
				elif(ai_choice == "rock"):
					winner = "ai"
					ai_wins = win(winner, ai_wins, your_wins)
		else:
			print "wrong choice!"
	if(your_wins == 3):
		print "You won whole match!"
		wanna_play = raw_input("Wanna play next match? (yes or no): ")
		if(wanna_play == "yes" ):
			play = 1
		else:
			play = 0
	elif(ai_wins == 3):
		print "You lost whole match!"
		wanna_play = raw_input("Wanna play next match? (yes or no): ")
		if(wanna_play == "yes"):
			play = 1
		else:
			play = 0
		
			