require 'test_helper'

class TestingsControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get testings_index_url
    assert_response :success
  end

end
