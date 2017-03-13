require 'rails_helper'

RSpec.describe SessionsController do

	describe "has working routes" do
		example "for get/login" do
			get :new
			expect(response).to have_http_status(:success)
		end
		
	end
end
