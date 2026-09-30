#Here are my beginning variables

expenses = []
expense_count = 0
expense = 1

print("\nPersonal Expense Analyzer\n")

#Here my program asks for each expense, validates them, and counts the amount.

while expense != 0:
    expense=float(input("Enter an expense or zero to finish: "))

    if expense <= -1:
        print("Sorry, all expenses must be positive")
    elif expense > 0:
        expenses.append(expense)
        expense_count += 1

#Here my program evaluates each expense as low, med, or high and count each total

small_expenses = 0
medium_expenses = 0
large_expenses = 0

for number in expenses:

    if number < 25:
        small_expenses += 1

    elif number < 100:
        medium_expenses += 1

    elif number >= 100:
        large_expenses += 1

#Here my program finds the total and average for the expenses

total_expense_amount = sum(expenses)
average = total_expense_amount / len(expenses)

#Here is the expense summary

print("\nExpense Summary\n")

print (f"Number of expenses: {expense_count}")
print (f"Total amount of expenses: ${total_expense_amount:,.2f}")
print (f"Expenses average: ${round(average, 2):,.2f}")
print (f"Smallest expense: ${min(expenses):,.2f}")
print (f"Largest expense: ${max(expenses):,.2f}")
print (f"\nSmall expenses: {small_expenses}")
print (f"Medium expenses: {medium_expenses}")
print (f"Large expenses: {large_expenses}\n")