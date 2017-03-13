def print255
	(1..255).each{|x| puts x }

end
# print255

def oddNumbers
	(1..255).each{|x| puts x if x%2==1}
end
# oddNumbers
def printSum
	sum = 0
	(1..255).each do |x| 
		puts "New Number: #{x} Sum: #{sum+=x}"
		
	end
end
# printSum
def itrtArr arr
	arr.each{|x| puts x}
end
# itrtArr [4, 5, 9, 0]

def max arr
	arr.max
end
# puts max [1,2,3,4]

def avg arr   
	sum = arr.reduce :+
	sum.to_f / arr.count

end
# puts avg [5,8,5,6]

def newArr
	newArr = Array.new
	(1..255).each{|x| newArr.push(x)}
	 newArr
end
#print newArr

#Greater than Y
class Array
	def greaterThan y
		count = 0
		puts 'test'
		self.each{|x| count+=1 if x > y }
		count
	end
	def shiftLeft amt
		for j in 1..amt
			current = self[0]
			for i in 0..self.count-1
				self[i]=self[i+1]
			end

			self[i]=current
		end

		self
	end
end



puts "This is the result: #{[1,2,3,5,7,90].shiftLeft (4)}" 










