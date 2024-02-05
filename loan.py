# Get details of loan
moneyOwed = float(input("How much money do you owe, in dollars?\n"))
apr = float(input("What is the annual percentage rate of the loan?\n"))
payment = float(input("How much will you pay off each month in dollars?\n"))
months = int(input("How many months do you want to see the results for?\n"))

monthlyRate = apr/100/12

for i in range(months):
    #Calc int to pay
    intPaid = moneyOwed * monthlyRate

    # Add in interest
    moneyOwed = moneyOwed + intPaid

    if (moneyOwed - payment < 0):
        print("The last payment is", moneyOwed)
        print("You paid off the loan in", i+1, "months.")
        break

    #Make payment
    moneyOwed = moneyOwed - payment

    print("Paid", payment, "of which", intPaid, "was interest.", end = " ")
    print("Now I owe", moneyOwed)
