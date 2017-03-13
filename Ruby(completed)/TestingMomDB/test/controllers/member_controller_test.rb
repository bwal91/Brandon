require 'test_helper'

class MemberControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get member_index_url
    assert_response :success
  end

  test "should get import" do
    get member_import_url
    assert_response :success
  end

end
