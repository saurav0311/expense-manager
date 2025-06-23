import json
from datetime import datetime

class Expense:
    def __init__(self, amount, category, note):
        self.amount=amount
        self.category=category
        self.note=note
        self.date=datetime.now().strftime("%Y-%m-%d")

    def show(self):
        print(f"Rs{self.amount} | {self.category} | {self.note} | {self.date} ")

    def to_dict(self):
        return{
            "amount": self.amount,
            "category": self.category,
            "note": self.note,
            "date": self.date,
        }
    
    @classmethod
    def from_dict(cls, data):
        obj=cls(data["amount"], data["category"], data["note"])
        obj.date= data["date"]
        return obj
    
expenses=[]

def save_to_file():
    with open("expenses.json","w") as f:
        json.dump([e.to_dict() for e in expenses], f, indent=4) #yesma meaning of for (why used?)For each expense e in the list expenses, call e.to_dict() and collect the result into a new list.
    print("Expenses Saved!!")

def load_from_file():
    global expenses
    try:
        with open("expenses.json", "r") as f:
            data=json.load(f)
            expenses= [Expense.from_dict(d) for d in data]
        print("Expenses loaded!!!")
    except FileNotFoundError:
        print("No saved file found. Starting fresh!!!")

def add_expense():
    try:
        amount=float(input("Enter an amount: Rs"))
        category=input("Enter category:")
        note=input("Enter any remarks:")
        expenses.append(Expense(amount, category, note))
        print("Expenses added.")
    except ValueError:
        print("Invalid amount. Try again!!!")

def show_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n Your Expenses: ")
    print("Amount | Category | Note | Date")
    print("-"*40)
    for e in expenses:
        e.show()

def main():
    load_from_file()
    while True:
        print("\n Expense Tracker Menu: ")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Save and Exit")
        choice=input("Choose an option between (1-3): ")

        if choice=="1":
            add_expense()
        elif choice=="2":
            show_expenses()
        elif choice=="3":
            save_to_file()
            print("GoodBye!!!!!")
            break
        else:
            print("Invalid Choice")

if __name__=="__main__":
    main()
        



