require 'test_helper'

class SubmittedControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get submitted_index_url
    assert_response :success
  end

end
