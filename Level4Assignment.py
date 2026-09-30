expenses = []

expense = 1

print("Personal Expense Analyzer")

while expense != 0:

    if (expense < 0):
        print("Sorry, Expenses must be a positive number.")



    expense = float(input("Enter an expense or 0 to finish: "))

    expenses.append(expense)

    print(expenses)

    
