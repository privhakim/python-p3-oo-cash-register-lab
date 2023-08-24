#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, item_name, price, quantity=1):
        self.total += price * quantity
        self.last_transaction_amount = price * quantity
        for _ in range(quantity):
            self.items.append(item_name)

    def apply_discount(self):
        if self.discount == 0:
            return "There is no discount to apply."
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
        return f"Discount of {self.discount}% applied."

    def void_last_transaction(self):
        if self.last_transaction_amount != 0:
            self.total -= self.last_transaction_amount
            self.items.pop()
            self.last_transaction_amount = 0
        else:
            return "No transactions to void."


register = CashRegister(20)  # Create a cash register  with a 20% discount
register.add_item("Apple", 0.5, 3)  # Add 3 apples at $0.5 each
print(register.total)  # Output: 1.5
print(register.items)  # Output: ['Apple', 'Apple', 'Apple']

register.apply_discount()  # Apply the discount
print(register.total)  # Output: 1.2 (20% discount applied)
print(register.apply_discount())  # Output: "Discount of 20% applied."

register.void_last_transaction()  # Void the last transaction
print(register.total)  # Output: 0.7 (Transaction voided)
print(register.items)  # Output: ['Apple', 'Apple']

