class Blog < ApplicationRecord
	has_many :post, dependent: :destroy

	validates :name, :description, presence: true

end
