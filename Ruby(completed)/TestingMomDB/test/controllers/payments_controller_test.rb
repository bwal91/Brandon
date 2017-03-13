require 'test_helper'

class PaymentsControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get payments_index_url
    assert_response :success
  end

  test "should get import" do
    get payments_import_url
    assert_response :success
  end

end
