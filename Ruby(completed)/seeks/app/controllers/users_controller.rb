class UsersController < ApplicationController
	def show
		@user = User.find(session[:user_id])
	end


	private
	def user_params
		params.require(:user).permit(:first_name, :last_name, :email, :password, :password_confirmation)
	end
end
