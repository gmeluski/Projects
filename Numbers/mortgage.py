annualRate = float(raw_input('What percentage is the annual interest rate? ')) / 100
years = int(raw_input('How many years? '))
principle = float(raw_input('How much are you borrowing? '))

monthlyPayments = years * 12
monthlyRate = annualRate / 12
rateStandard = (1 + monthlyRate) ** monthlyPayments

paymentAmount = ((principle * monthlyRate) * rateStandard) / (rateStandard - 1)  

print "Your monthly payment is $%.2f" % (paymentAmount)
