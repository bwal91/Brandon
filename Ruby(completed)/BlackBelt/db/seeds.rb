require 'rubygems'
require 'faker'

# password = "password"

# 20.times do |index|
#   Post.create!(idea: Faker::Lorem.sentence(4, false, 0).chop,
#                  user_id: rand(1..20))
                

# end

# 20.times do |index|
#   User.create!(name: Faker::Name.name,
#                	alias: Faker::Name.first_name,
#                 email: Faker::Internet.safe_email,
#                 password: 'password',
#                 password_confirmation: 'password' )
# end

# 20.times do |index|
#   Like.create!(user_id: rand(1..20),
#   				  post_id: rand(1..20) )
               	
# end

# @@count = 0
# 20.times do
#   @@count += 1 
#   this = Post.find(@@count)
#     this.update(likes_count: rand(1..30))

# end
# 20.times do
# 	@this = Event.where(user_id: nil)
# 		@this.each do |that|
# 			that.update(user_id: rand(1..20))
# 		end
# end


# @@count = 0
# 20.times do
#   @@count += 1 
#   this = User.find(@@count)
#     this.update(event_id: rand(1..20))

# end
# @@count = 0
# 20.times do
# 	@@count += 1
# 	this = User.find(@@count)
# 	that = Event.find(@@count)
# 		this.parties.create(event: that)
# 	end


# me = User.create(first_name: "Brandon",
# 				last_name: "Walter",
# 				email: "brandon@livehuge.com",
# 				city: "Redmond",
# 				state: "WA",
# 				password: "password",
# 				password_confirmation: "password")
# event = Event.create(name: "Testing This",
# 					city: "Seattle",
# 					state: "WA")
# 	me.parties.create(event: event)




# p "Created #{User.count} Users"
# p "Created #{Event.count} Events"
# p "Created #{User.count} Users"
# p "Created #{Comment.count} Comments"