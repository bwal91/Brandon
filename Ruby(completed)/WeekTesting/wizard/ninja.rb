require_relative 'wizard'

class Ninja < Wizard

	def initialize
		super
		@health = 100
		@stealth = 175
	end

	def steal(obj)
		param = [50]
		obj.stealth = param.flatten.inject(obj.stealth) {|stealth, param| stealth - param}
		@health += 10
	end

	def get_away
		@health += 15
		self
	end

	def health
		@health
	end
end