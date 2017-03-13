class Human
	
	attr_accessor :strength, :intelligence,:stealth, :health
	def initialize
    	@strength = 3
    	@intelligence = 3
    	@stealth = 3
    	@health = 100
  	end

  	def attack(obj)
	  	puts obj
	    if obj.class.ancestors.include?(Human)
	      obj.health -= 10
	      true
	      puts "Yay"
	    else
	      false
	      puts "No"
	    end
  	end
end
