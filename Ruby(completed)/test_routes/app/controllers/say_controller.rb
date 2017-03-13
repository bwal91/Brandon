class SayController < ApplicationController
  


  def index
  	render text: "What do you want me to say???"

  end

  

  def hello
  
  	render text: "Hello CodingDojo!"

  end

  def show

  	render text: "Saying Hello!"

  end

  def name

  	render text: "Saying Hello Joe!"
  
  end


end
