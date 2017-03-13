class TimeController < ApplicationController 

	def index
		
		@time = Time.now.strftime('%H:%M')
		@date = Time.now.strftime("%m/%d/%Y")
		
		render "index"
	end


end
