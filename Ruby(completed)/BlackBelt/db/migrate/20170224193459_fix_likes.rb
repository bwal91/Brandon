class FixLikes < ActiveRecord::Migration[5.0]
  
  def change
  	remove_column :likes, :post_id
  	remove_column :likes, :user_id
  	remove_column :posts, :likes_count
  end
end
