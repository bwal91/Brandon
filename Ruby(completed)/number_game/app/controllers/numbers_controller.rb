class NumbersController < ApplicationController
  


	def index

		if session[:number] == nil
			session[:number] = Random.new.rand(1..101)
		else
			session[:number] = session[:number]
		end
		puts session[:number]
		render 'index'
	end

	def submit
		if @guess == nil
			@guess = params[:number]
		else 
			@guess = params[:number]
		end
		if @guess.to_i <	session[:number]
			flash[:low] = " "
		elsif @guess.to_i > session[:number]
			flash[:high] = " "
		else
			flash[:correct] = " "
		end
		
		redirect_to "/"

	end

	def play_again

		@guess = 0
		session.clear
		redirect_to "/"

	end
end
