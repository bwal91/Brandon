Rails.application.routes.draw do
  

  get 'times/' => 'times#index'



  get 'times/restart' => 'times#restart'

  get 'say/index'

  get '/' => 'say#index'
  get '/hello/' => 'testings#hello'
  get '/say/hello' => 'say#show'
  get '/say/hello/joe' => 'say#name'
  get '/say/hello/michael' => redirect("/say/hello/joe")



  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
