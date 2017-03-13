class SurveysController < ApplicationController
	@@count = 0
	def index

		@location = ["Seattle", "Mountain View", "Dallas", "Chicago"]
		@language = ["Python", "Ruby", "JavaScript", "Mean"]

		render "index"
	end

	
	def submit
		session[:name] = params[:name]
		session[:location] = params[:location]
		session[:language] = params[:language]
		session[:comment] = params[:comment]
		@@count += 1
		redirect_to "/surveys/result"

	end


	def result
		
		flash[:count] = "You have submitted the survey #{@@count} time(s)!"


	end

	def goback

		session[:name] = nil
		session[:location] = nil
		session[:language] = nil
		session[:comment] = nil

		redirect_to "/surveys/index"
	end

	def reset
		
		@@count = 0
		session.clear
		redirect_to "/surveys/index"
		
	end

end
