json.extract! todo, :id, :name, :due_on, :completed, :created_at, :updated_at
json.url todo_url(todo, format: :json)