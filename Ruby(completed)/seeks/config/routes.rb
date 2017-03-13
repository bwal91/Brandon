Rails.application.routes.draw do
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  get '/', to: 'sessions#new'
  post '/sessions', to: 'sessions#create'
  get '/user', to: 'users#show'
end
