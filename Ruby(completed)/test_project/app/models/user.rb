class User < ActiveRecord
  EMAIL_REGEX = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i
  validates :first_name, :last_name, presence: true, length: { in: 2..20 }
  validates :email, presence: true, uniqueness: { case_sensitive: false }, format: { with: EMAIL_REGEX }
  before_save do
    self.email.downcase!
  end
  before_create do
    self.admin = false #assuming there is an admin field with a boolean value
  end
  def full_name
    self.first_name + " " + self.last_name
  end
  def admin?
    self.admin
  end
  def self.average_age
    users = User.all
    total_age = 0
    users.each do |user|
      total_age += user.age
    end
    total_age / User.count
  end
end