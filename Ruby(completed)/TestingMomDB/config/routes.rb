Rails.application.routes.draw do

  get '/payments', to: 'payments#index'

  		resources :payments do
		collection {post :import}
	end
		resources :members do
		collection {post :import}
	end

	root to: "members#index"

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
