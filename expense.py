class Expense:

    def __init__(self, name, cagetory, amount) -> None:
        self.name = name
        self.category = cagetory
        self.amount = amount
        
    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f} >"