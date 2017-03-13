class UsersController < ApplicationController
  before_action :logged_in, except: [:new, :create]

  def edit
  end

  def update
  end

  def create
  end

  def destroy
  end

  def new
  end
end
