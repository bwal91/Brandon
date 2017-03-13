class Member < ApplicationRecord
	require 'csv'

	def self.import(file)

		CSV.foreach(file.path, {col_sep: ',', headers: true}) do |row|
			
			Member.create! row.to_hash

		end
	end


	
end
