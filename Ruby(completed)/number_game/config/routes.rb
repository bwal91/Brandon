Rails.application.routes.draw do
  

  get 'numbers/index' 

  get '/' => 'numbers#index'
  post '/submit/' => 'numbers#submit'
  get '/play_again/' => 'numbers#play_again'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
