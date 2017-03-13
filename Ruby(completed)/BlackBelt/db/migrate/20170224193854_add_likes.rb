class AddLikes < ActiveRecord::Migration[5.0]
  def up
  	create_table :likes do |t|
  		t.boolean :like
  		t.references :likeable, polymorphic: true
  		t.integer :user_id
  		t.timestamps
  	end
  end
end
