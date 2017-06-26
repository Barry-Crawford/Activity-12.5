initialInvestment = input("How much are you going to invest? ")
term = input("How many years are you going to invest the money? ")
interestRate = input("Input the annual interest rate as a decimal. [For 2% enter .02] ")
Months = term * 12
print "Months\tInterest Earned\t  Total"
y = 1
while y <= Months:
	interestEarned = initialInvestment * (interestRate/12)
	initialInvestment = interestEarned + initialInvestment
	print y, "\t" , "$" , "{:.2f}".format(interestEarned) , "\t" , "$" , "{:.2f}".format(initialInvestment)
	y = y + 1