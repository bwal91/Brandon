class UsersController < ApplicationController
  

	def index

		@users = User.all

		render "index"
	end

	def new
		render "create"
	end

	def create
		
		@user = User.new(user_params)
		if @user.save 
			redirect_to '/users/'
		else
			flash[:error] = "All fields must be complete!"
			redirect_to '/users/new/'
		end

	end

	private

	def user_params
		params.require(:user).permit(:first_name, :last_name, :email, :password)
	end	


end
