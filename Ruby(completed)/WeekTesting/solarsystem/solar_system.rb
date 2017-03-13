class SolarSystem
	attr_accessor :name, :planets
	def initialize name="Andromeda"
		@name = name
		@planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

	end

	def count
		@planets.count
	end

	def super_nova
		@planets.clear
	end

end

class Planet < SolarSystem
	attr_accessor :description, :population
	
	def add_planet(planet)
		@@name.push(planet)
	end
	

end
