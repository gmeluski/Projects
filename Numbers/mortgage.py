annualRate = float(raw_input('What\'s your annual interest rate?')) * 100
terms = int(raw_input('How many terms?'))
loanTotal = float(raw_input('How much are you borrowing?'))

monthlyRate = annualRate / 12
payments = (loanTotal *  (monthlyRate * (1 + monthlyRate) * terms)) / (((1 + monthlyRate) * terms) - 1) 


# P= L[c (1 + c)n] / [(1+c)n - 1]
