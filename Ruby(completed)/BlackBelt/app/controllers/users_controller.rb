class UsersController < ApplicationController
  before_filter :authorize, :only => :show

	def index


	end

	def register
		@user = User.new(user_params)
		if @user.save
			session[:user_id] = @user.id
			redirect_to '/bright_ideas'
		else
			flash[:error] = @user.errors.full_messages
			redirect_to '/'
		end
	end

	def show
		@user = User.find(params[:id])
		@post = Post.where(:user_id => session[:user_id]).count
		@likes = Like.where(:user_id => session[:user_id]).count
	end


	private
	def user_params
		params.require(:user).permit(:name, :alias, :email, :password, :password_confirmation)
	end	


end
