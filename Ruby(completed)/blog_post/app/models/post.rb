class Post < ApplicationRecord
  belongs_to :blog
  has_many :messages, dependent: :destroy

  validates :title, :content, presence: true, length: { minimum: 7 }

end
