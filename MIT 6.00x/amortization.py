'''
Given a loan and the annual interest rate on it, 
calculate the least amount you need to spend if you want to pay it off in a year.
'''

low = balance/12.0
high = (balance * (1 + annualInterestRate/12)**12)/12.0
pay = (high + low)/2.0


def account(balance, pay, annualInterestRate):
   ##calculate the balance after paying a fixed amount for 12 months
   for i in range(12):
      balance = (balance - pay) * (1 + annualInterestRate/12)
   return balance

def lowAmort(balance, pay, annualInterestRate):
   ##calculate the lowest amount you need to pay to payoff a loan
   newBalance = account(balance, pay, annualInterestRate)
   while abs(newBalance) > 0.001:
      if newBalance > 0:
         low = pay
      else:
         high = pay
   pay = (high + low)/2.0
   newBalance = account(balance, pay, annualInterestRate)
   print "Lowest Payment:" + str(round(pay,2))
   return pay
