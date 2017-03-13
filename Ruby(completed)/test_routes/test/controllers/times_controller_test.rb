require 'test_helper'

class TimesControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get times_index_url
    assert_response :success
  end

  test "should get restart" do
    get times_restart_url
    assert_response :success
  end

end
