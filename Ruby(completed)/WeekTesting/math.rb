class MathDojo
	
	attr_accessor :sum
	def initialize 
		@sum = 0
	end

	def add *param
		@sum = param.flatten.inject(@sum) {|sum, param| sum + param }
		self

	end

	def subtract *param

		@sum = param.flatten.inject(@sum) {|sum, param| sum - param}
		self

	end

	def result
		puts @sum
	end
end
MathDojo.new.add(2,5).subtract(5,2).result
# .add([3,5,6],[2,4,5]).subtract([-2,5,12],[2,5,7]).result
