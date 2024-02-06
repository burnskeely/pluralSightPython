expenses = [10.50, 8, 5, 15, 20, 5, 3]

total = sum(expenses)

print("You spent £", total, sep = "")

#OR 

sum = 0

for x in expenses:
    sum = sum + x

print("You spent £", sum, sep = "")

#OR 
total = 0 
expenses = []

numExpenses = int(input("Enter number of expenses:"))

for i in range(numExpenses):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)

print("You spent £", total, sep = "")