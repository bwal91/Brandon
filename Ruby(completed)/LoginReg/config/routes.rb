Rails.application.routes.draw do

  get 'products/index'

	post '/login', to: 'sessions#create'
 	post '/register', to: 'users#create'
 	get '/login', to: 'sessions#new'
 	get '/register', to: 'users#new'
 	delete '/logout/:id', to: 'sessions#destroy'

 	root 'products#index'

end
