class User
	attr_accessor :first_name, :last_name
	def initialize(f_name, l_name)
		@first_name = f_name
		@last_name = l_name
	end
	def my_name
		puts "I am #{@first_name} #{@last_name}"
	end

end

brandon = User.new("Brandon", "Walter")
brandon.my_name