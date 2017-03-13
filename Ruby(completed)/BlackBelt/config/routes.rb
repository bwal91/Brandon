Rails.application.routes.draw do
  get '/bright_ideas', to: 'posts#index'

  post '/login', to: 'sessions#create'
  post '/register', to: 'users#register'

  get '/logout', to: 'sessions#destroy'

  get '/like/:id', to: 'posts#like'
  get '/show/:id', to: 'posts#show'

  get '/user/:id', to: 'users#show'

  post '/create/idea', to: 'posts#create'



  root to: 'users#index'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
