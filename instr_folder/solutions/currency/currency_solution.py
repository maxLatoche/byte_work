import math

def my_money(amount):
	denominations = [.01, .05, .1, .25, 1, 5, 10, 20, 50, 100]
	current_bill = 0
	bill_amount = 0
	wallet = dict()

	while len(denominations) > 0:
		current_bill = denominations.pop()
		bill_amount = math.floor(amount/current_bill)
		wallet[current_bill] = bill_amount
		amount = amount - (current_bill * bill_amount)

	return wallet

print(my_money(837.45))

