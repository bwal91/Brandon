Rails.application.routes.draw do
  
  get 'submitted/index'

	get '/' => 'surveys#index'
	get 'surveys/index'
	post '/submit/' => 'surveys#submit'
	get '/surveys/result/' => 'surveys#result'
	get '/goback/' => 'surveys#goback'
	get '/reset/' => 'surveys#reset'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
