class MemberController < ApplicationController
  def index
  	@members = Member.all
  end

  def import
  	Member.import(params[:file])

  	redirect_to root_url, notice: "Member Data imported"
  end
end
