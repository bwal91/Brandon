def printSum
	b = [3,5,1,2,7,9,8,13,25,32]
	sum = 0
	b.each do |x|
		sum+=x
	end
	print sum
	newArr = Array.new
	b.each do |y|
		newArr.push(y) if y > 10
	end
	print newArr
end
printSum


def shuffle
	a = ["John", "KB", "Oliver", "Matthew", "Christopher"]
	puts a.shuffle
	newArr = Array.new
	a.each do |f|
		 newArr.push(f) if f.length > 5
	end
	print newArr
end
shuffle

def alphabet
	c = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	puts c.shuffle.last
	sh = c.shuffle.first
	puts sh
	if sh.start_with? "A", "E", "I", "O", "U"
		puts "It starts with a Vowel!" 
	end
end
puts "Here is the answer: #{alphabet}" 

def randomArray 
	newArr = Array.new
	for i in 1..10
		num = Random.new.rand(55..100)
		newArr.push(num)
	end
	print newArr
end
randomArray

def randomArray 
	newArr = Array.new
	for i in 1..10
		num = Random.new.rand(55..100)
		newArr.push(num)
	end
	print newArr.sort
	puts "Min is: #{newArr.min}"
	puts "Max is: #{newArr.max}"
end
randomArray

def randomString 
	puts (1..5).map{(65 + rand(26)).chr}.join
end
randomString

def randomWords 
	newArr = Array.new
	for i in 1..10
		a = (1..5).map{(65 + rand(26)).chr}.join
		newArr.push(a)
	end
	print newArr
end
randomWords












