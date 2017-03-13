require_relative 'human'

class Wizard < Human

	def initialize
		super
		@health = 50
		@intelligence = 25
	end

	def heal
		@health += 10
	end

	def fireball(obj)
		param = [20]
		obj.health = param.flatten.inject(obj.health) {|health, param| health - param}
	end
end

