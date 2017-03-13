class Human
	
	def initialize
		@strength = 3
		@intelligence = 3
		@stealth = 3
		@health = 100
	end
	
	def attack
		@health -= 50
		puts @health
		self
	end

	def learn
		@intelligence += 50
		puts @intelligence
		self
	end
end

test = Human.new
test.attack
test.learn