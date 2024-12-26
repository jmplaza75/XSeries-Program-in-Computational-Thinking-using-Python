#!/usr/bin/env python3

monthlyInterestRate = annualInterestRate / 12.0

low = balance / 12
high = (balance * (1 + annualInterestRate)**12 ) / 12


bol = False
while not bol :
	mid = (high + low) / 2
	fixedMonthlyPayment = round(mid, 2)
	remBalance = balance
	#loop to find remaining balance at the end of 12 months
	for month in range(1,13):
		unpaidBalance = remBalance - fixedMonthlyPayment
		remBalance = unpaidBalance + unpaidBalance*monthlyInterestRate
	#conditions on remaining balance
	if abs(remBalance) <= 0.1:              #0.1 is the expulsion value
		bol = True
	elif remBalance > 0:
		low = mid + 0.01
	elif remBalance < 0:
		high = mid - 0.01
		
print(fixedMonthlyPayment)