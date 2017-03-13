require_relative 'bankacc'

RSpec.describe BankAccount do 
	before(:all) do 
		@bank = BankAccount.new
	end

	it 'check retrieving checking account balance' do 

		@bank.check_bal

		expect(@bank.check_bal).to eq(0)
	end

	it 'check retrieving total account balance' do 

		@bank.total

		expect(@bank.total).to eq(0)
	end

	describe '#withdraw_check' do
	before(:all) do 
		@bank = BankAccount.new
	end		
		it 'check withdarawing cash insufficient' do 
		
			@bank.withdraw_check(100)

			expect {BankAccount.withdraw_check}.to raise_error("Sorry!")
			
		end

		it 'check withdraw cash works' do 
			expect do
				
	
				@bank.withdraw_check(0)

			end.to output("Enjoy your Money!\n").to_stdout
		end
	end

	it 'error checking total bank accounts' do 

		@bank.total_acc

		expect {@bank.total_acc}.to raise_error()
	end

	it 'error checking interest rate' do 

		@bank.set_interest

		expect {@bank.set_interest}.to raise_error()
	end

	it 'error checking set attribute' do

		bank = BankAccount.new("Hello")

		expect {BankAccount.new}.to raise_error()
	end


end













