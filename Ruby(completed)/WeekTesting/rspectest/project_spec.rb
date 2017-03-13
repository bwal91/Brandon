require_relative 'project'

RSpec.describe Project do
	
	it 'has a getter and setter for name and attribute' do

		project1 = Project.new("Project Name", "I am a project")
		project2 = Project.new("Project 2", "Test Project2")
		project1.add_to_team("Dojo")

		expect(project1.elevator_pitch).to eq("Project Name, I am a project")
		expect(project2.elevator_pitch).to eq("Project 2, Test Project2")
		expect(project1.team).to eq("Dojo")
	end

end
