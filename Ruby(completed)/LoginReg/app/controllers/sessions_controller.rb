class SessionsController < ApplicationController
	before_action :logged_in, only: [:destroy]
  def new
  end

  def create
  	@user = User.find_by_email params[:email]
  	if @user and @user.authenticate params[:password]
  		session[:user_id] = @user.id
  		redirect_to :root
  	else
  		flash[:error] = "Login info not found"
  		redirect_to :back
  	end
  end

  def destroy
  end
end
