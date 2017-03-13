heads = 0
tails = 0
attempts = 0
for count in range (1,5002):
	import random
	random_num = random.random()
	coin = round(random_num)
	if coin == 1:
		print "Attempt # "+str(attempts)+": Throwing a coin... It's a head!... Got "+str(heads)+" head(s) so far and "+str(tails)+" tail(s) so far!"
		heads += 1
	if coin == 0:
		print "Attempt # "+str(attempts)+": Throwing a coin... It's a tail!... Got "+str(heads)+" head(s) so far and "+str(tails)+" tail(s) so far!"
		tails += 1
	attempts += 1
