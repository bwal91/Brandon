Rails.application.routes.draw do


  get 'comments/index'

  get 'comments/create'

	get '/' => 'products#index'
	get '/show/:id' => 'products#show'
	get '/back/' => 'products#back'
	get '/new' => 'products#new'
	post '/create/' => 'products#create'
	get '/edit/:id' => 'products#edit'
	patch '/update/:id' => 'products#update'
	get '/destroy/:id' => 'products#destroy'
	post '/comment/:id' => 'comments#create'
	get '/comments/' => 'comments#index'
  	
end
