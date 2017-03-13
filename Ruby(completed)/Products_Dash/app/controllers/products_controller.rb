class ProductsController < ApplicationController
  
  def index

    @products = Product.all
    # @category = Category.all

  end

  def show

    @products = Product.find(params[:id])
    if @products.category_id
      @current = Category.find(@products.category_id)
    else
      @current = nil
    end
    # @comments = Comment.find_by product_id: params[:id]
    @comments = Comment.where(product_id: params[:id])

  end

  def new
    @category = Category.all
  end

  def edit
    @products = Product.find(params[:id])
    if @products.category_id
      @current = Category.find(@products.category_id)
    else
      @current = nil
    end
    @category = Category.all
  end

  def create
    @product = Product.new(product_params)
    if @product.save
      redirect_to '/'
    else
      flash[:error] = "All fields must be complete!"
      redirect_to :back
    end

  end

  def update
    @product = Product.find(params[:id])
    if @product.update(product_params)
      redirect_to '/'
    else
      flash[:error] = @product.errors.full_messages
      redirect_to :back
    end

  end

  def destroy
    Product.find(params[:id]).destroy
    redirect_to :back
  end

  def back
    redirect_to '/'
  end

  private
  def product_params
    params.require(:product).permit(:name, :description, :pricing, :category_id)
  end

end
