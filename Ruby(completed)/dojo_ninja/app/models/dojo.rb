class Dojo < ApplicationRecord
	has_many :ninjas, dependent: :destroy

	validates :name, :city, presence: true
	validates :state, length: { in: 2..2 }

end
