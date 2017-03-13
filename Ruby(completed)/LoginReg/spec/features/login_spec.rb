require 'rails_helper'

RSpec.describe "Login Experience" do

before(:each) do
	User.create(name: "JimBob", email: "hello@jim.com", password: "password")
	end

	example "works with correct info" do
		visit "/login"
		within "#form_id" do
			fill_in "email", with: "hello@jim.com"
			fill_in "password", with: "password"
		end
		click_button "Login"
		expect(page).to have_content("JimBob")
	end

	example "errors display" do
		visit "/login"
		click_button "Login"
		expect(page).to have_content("Login info not found")
	end



end