require_relative 'solar_system'

RSpec.describe Planet do
	describe 'attributes' do
		before do 
			@planet = Planet.new
			@planet.name = "Mars"
			@planet.description = "Red Planet"
			@planet.population = 0
		end

		it "is expected to have name, description, and population attributes" do 
			expect(@planet).to have_attributes(:name => "Mars")
			expect(@planet).to have_attributes(:description => "Red Planet")
			expect(@planet).to have_attributes(:population => 0)
		end
	end

	describe 'behaviour' do
		before do
			@planet = Planet.new
		end

		it "should only add planet from Planet class" do
			@planet.name = "Mars"
			@planet.planets = @planet.name
			expect(@planet.planets).to eq("Mars")
		end
	end
end

RSpec.describe SolarSystem do
	describe 'initialization' do 
		before do
			@solarSystem = SolarSystem.new
		end

		it "should be initialized with a name, if not its default name should be 'Solar System'" do
			expect(@solarSystem.name).to eq("Andromeda")
			@solarSystem.name = "Gemini"
			expect(@solarSystem.name).to eq("Gemini")
		end

		it "should contain a list of all planets" do
			@planet = Planet.new

			expect(@solarSystem.planets).to match_array(["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"])
		end
	end

	describe 'behavior' do 
		before do
			@solarSystem = SolarSystem.new
		end
		it "should count how many planets are in the Solar System." do
			expect(@solarSystem.count).to eq(8)
		end

		it "should have a method called Super Nova that destroys all of the planets in it" do
			@solarSystem.super_nova
			expect(@solarSystem.planets.empty?).to eq(true)
		end
	end
end