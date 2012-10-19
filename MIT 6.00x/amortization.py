'''
totalPaid = 0
for i in range(12):
   print 'Month: ' + str(i)
   monthlyPayment = monthlyPaymentRate * balance
   print 'Minimum monthly payment: ' + str(round(monthlyPayment,2))
   balance = (balance - monthlyPayment) * (1 + annualInterestRate/12)
   print 'Remaining balance: ' + str(round(balance,2))
   totalPaid = monthlyPayment
print 'Total paid: ' + str(round(totalPaid, 2))
print str(round(balance,2))
'''
##Test Case 1:
##balance = 3329
##annualInterestRate = 0.2
##
##Result Your Code Should Generate:
##-------------------
##Lowest Payment: 310
##
##
##Test Case 2:
##balance = 4773
##annualInterestRate = 0.2
##Result Your Code Should Generate:
##-------------------
##Lowest Payment: 440
##
##
##Test Case 3:
##balance = 3926
##annualInterestRate = 0.2
##
##Result Your Code Should Generate:
##-------------------
##Lowest Payment: 360
'''
lowPay = 0

def account(balance, lowPay, annualInterestRate):
    for i in range(12):
        balance = (balance - lowPay) * (1 + annualInterestRate/12)
    return balance

def fixMinPay(balance, lowPay):
    newBalance = account(balance, lowPay, annualInterestRate)
    while newBalance > 0:
        lowPay += 10
        newBalance = account(balance, lowPay, annualInterestRate)
    return lowPay

print "Lowest Payment: " + str(fixMinPay(balance, lowPay))
'''
##Test Case 1:
##balance = 320000
##annualInterestRate = 0.2
##
##Result Your Code Should Generate:
##-------------------
##Lowest Payment: 29157.09
##
##Test Case 2:
##balance = 999999
##annualInterestRate = 0.18
##
##Result Your Code Should Generate:
##-------------------
##Lowest Payment: 90325.07

balance = 320000
annualInterestRate = 0.2

low = balance/12.0
high = (balance * (1 + annualInterestRate/12)**12)/12.0
pay = (high + low)/2.0


def account(balance, pay, annualInterestRate):
    for i in range(12):
        balance = (balance - pay) * (1 + annualInterestRate/12)
    return balance

newBalance = account(balance, pay, annualInterestRate)
while abs(newBalance) > 0.001:
    if newBalance > 0:
        low = pay
    else:
        high = pay
    pay = (high + low)/2.0
    newBalance = account(balance, pay, annualInterestRate)
print "Lowest Payment:" + str(round(pay,2))
