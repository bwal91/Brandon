require_relative 'ninja'

class Samurai < Ninja
	@samurais = 0
	class << Samurai
		attr_accessor :samurais
	end

	def initialize
		super
		@health = 200
		self.class.samurais += 1
	end

	def death_blow(obj)
		obj.health = 0
		
	end

	def meditate
		@health = 200
	end


	def how_many
		puts Samurai.samurais
	end

end
samurai = Samurai.new
puts samurai.meditate
puts samurai.stealth
puts "********"
ninja = Ninja.new
puts samurai.death_blow(ninja)
ninja.get_away.get_away.get_away.get_away
puts "******"
wizard = Wizard.new
puts samurai.death_blow(wizard)
puts wizard.heal
puts ninja.health
puts wizard.fireball(ninja)
puts ninja.health
