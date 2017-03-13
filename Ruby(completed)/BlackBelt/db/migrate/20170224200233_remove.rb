class Remove < ActiveRecord::Migration[5.0]
  def change
  	drop_table :likes

  	create_table :likes do |t|
  		t.references :user, foreign_key: true
  		t.references :post, foreign_key: true

  		t.timestamps
  	end
  end
end
