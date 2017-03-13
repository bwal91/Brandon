class Comment < ApplicationRecord
  belongs_to :product

  validates :comment, :product_id, presence: true
  
end
