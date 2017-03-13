class Project
	
	attr_accessor :name, :description, :team_name
	def initialize name, description
		@name = name
		@description = description
		@team_name = []
	end
	
	def name
		@name
	end
	
	def elevator_pitch
		"#{@name}, #{@description}"
	end

	def add_to_team *member
		@team_name.push(member)
	end
	def team
		@team_name*","
	end

end
test = Project.new("Brandon", "Testing")
test.add_to_team("Hello", "Testing", "Another")
test.team