from expense import Expense
import calendar
import datetime

def main():
    print(f"📊 Running expense tracker!")
    file_path = "expenses.csv"

    budget = float(input("Enter Your Monthly Budget: "))

    expense = get_user_expense()

    expense_to_file(expense, file_path)

    summerize_expense(file_path, budget)


def get_user_expense():
    print(f"🎯 Getting User Expense")
    expense_name = input("Enter Expense Name ")
    expense_amount = float(input("Enter Expense Amount "))

    expense_cagetories = [
        "🍲 Food", 
        "🏠 Home", 
        "📚 School",
        "👔 Work", 
        "🎉 Fun", 
        "✨ Misc",
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_cagetories):
            print(f" {i+1}. {category_name}")

        value_range = f"[1 - {len(expense_cagetories)}]"
        index_selected = int(input(f"Enter a category number {value_range}: ")) - 1

        if index_selected in range(len(expense_cagetories)):
            category_selected = expense_cagetories[index_selected]
            new_expense = Expense(name = expense_name, cagetory= category_selected, amount=expense_amount)
            return new_expense
        else:
            print("Invalid Entry. Please try again!")
        

    
def expense_to_file(expense: Expense, file_path):
    print(f"🎯 Saving User Expense: {expense} to {file_path}")
    with open(file_path, "a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")

    

def summerize_expense(file_path, budget):
    print(f"🎯 Summerizing User Expense")
    expenses: list[Expense] = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")
            line_expense = Expense(name = expense_name, cagetory= expense_category, amount=float(expense_amount))
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses By Category")
    for key, amount in amount_by_category.items():
        print(f" {key}: ${amount:.2f}")

    total_spent = sum([expense.amount for expense in expenses])
    print(f"💸 Spent ${total_spent:.2f} this month!")

    remaining_budget = budget - total_spent
    if remaining_budget < 0:
        print(red("You have spent the budget!!!"))
    print(f"💵 Remaining ${remaining_budget:.2f} left this month!")

    #get current date
    now = datetime.datetime.now()

    #calculate the remaining number of days in the current month
    days_in_month = calendar.monthrange(now.year, now.month)[1]

    #calculate the remaining days in the current month
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print(green(f"👉 Budget per day: {daily_budget:.2f}"))


def green(text):
    return f"\033[92m{text}\033[0m"

def red(text):
    return f"\033[91m{text}\033[0m"


if __name__ == "__main__":       #this runs only when you run this file not when you run it as apart of another file       
    main()
