class ApplicationController < ActionController::Base
  protect_from_forgery with: :exception
  helper_method :current_user, :logged_in



  def current_user 
  	User.find(session[:user_id])
  end
  

  def logged_in
  	if !session[:user_id]
  		redirect_to '/login'
  	end
  end
end
