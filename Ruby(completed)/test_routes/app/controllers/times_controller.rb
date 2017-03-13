class TimesController < ApplicationController


	def index

		if session[:count]
			session[:count] += 1 
		
		elsif session[:count] == nil
			session[:count] = 0
		end

		render text: "You have visited the page "+session[:count].to_s+" times"


	end

	def restart

		reset_session

		render text: "Destroyed the session!"

	end
end
