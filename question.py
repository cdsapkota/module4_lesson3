class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__total_expenses = 0  # Tracks expenses

    # Getter for category name
    def get_category_name(self):
        return self.__category_name

    # Setter for category name
    def set_category_name(self, category_name):
        if isinstance(category_name, str) and category_name.strip():
            self.__category_name = category_name
        else:
            raise ValueError("Category name must be a non-empty string.")

    # Getter for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated budget
    def set_allocated_budget(self, allocated_budget):
        if isinstance(allocated_budget, (int, float)) and allocated_budget > 0:
            self.__allocated_budget = allocated_budget
        else:
            raise ValueError("Allocated budget must be a positive number.")
        
    # Calculate remaining budget dynamically
    def get_remaining_budget(self):
        return self.__allocated_budget - self.__total_expenses

    # Add an expense to the category
    def add_expense(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            if amount <= self.get_remaining_budget():
                self.__total_expenses += amount
            else:
                raise ValueError("Expense exceeds the remaining budget.")
        else:
            raise ValueError("Expense amount must be a positive number.")


    # Display budget category summary
    def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget:.2f}")
        print(f"Remaining Budget: ${self.get_remaining_budget():.2f}")


# Example usage
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()
