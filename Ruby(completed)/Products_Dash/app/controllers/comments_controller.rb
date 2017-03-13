class CommentsController < ApplicationController
  

  def index
  	@comments = Comment.all
  	@products = Product.all
  	render 'comments'
  end

  def create
  	@comments = Comment.new(comment_params)
  	if @comments.save
  		redirect_to :back
  	else
  		flash[:error] = @comments.errors.full_messages
  		redirect_to :back
  	end
  end

  private
  def comment_params
  	params.require(:new_com).permit(:comment, :product_id)
  end

end

# @comments = Comment.new(comment: params[:comment], product_id: params[:id])