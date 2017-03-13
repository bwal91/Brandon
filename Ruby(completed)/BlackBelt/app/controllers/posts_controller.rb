class PostsController < ApplicationController
  before_filter :authorize
  def index

  	@user = User.find(session[:user_id])
  	# @idea = Post.joins(:likes).merge(Like.order("post_id"))
  	# @like = Post.joins(:likes).group("post.id").order("count(post.id)")
  	@idea = Post.joins(:likes).group("post_id").order("count(post_id) DESC")
    @no_like = Post.includes(:likes).where(likes: { post_id: nil })
  	@likes = Post.joins(:likes).count
  	

  end

  def create
  	@idea = Post.new(idea_params)
  	if @idea.save
  		Like.create(user: current_user, post: @idea)
  		redirect_to :back
  	else
  		flash[:error] = @idea.errors.full_messages
  		redirect_to :back
  	end
  end

  def destroy
  	@idea = Post.find(params[:id])
  	@idea.destroy
  	redirect_to :back
  end

  def show
  	@post = Post.find(params[:id])
  	@likes = Like.where(post_id: params[:id])

  end

  def like
  	if Like.where(user_id: session[:user_id], post_id: params[:id]).count != 0
      flash[:error] = "Sorry, you can not like an Idea more than once!"
      redirect_to :back
    else
      Like.create(user_id: session[:user_id], post_id: params[:id])
      redirect_to :back
  	end
  end

  private
	def idea_params
		params.require(:idea).permit(:idea, :user_id)
	end	
end
