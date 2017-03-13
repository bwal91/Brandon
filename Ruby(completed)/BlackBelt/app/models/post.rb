class Post < ApplicationRecord

  belongs_to :user
  has_many :likes

  validates :idea, presence: :true, length: { minimum: 5}

end
