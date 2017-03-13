def Scores():
	for count in range (1,11):
		score = input("What is your score? ")
		grade = ""
		if 90 <= score <= 100:
			print "Score: "+str(score)+"; Your grade is A"
		if 80 <= score <=89:
			print "Score: "+str(score)+"; Your grade is B"
		if 70 <= score <= 79:
			print "Score: "+str(score)+"; Your grade is C"
		if 60 <= score <=69:
			print "Score: "+str(score)+"; Your grade is D"
	for count in range (1,11):
		Scores() 

Scores()