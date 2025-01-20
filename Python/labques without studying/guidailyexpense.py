import tkinter as tk
from tkinter import messagebox
import datetime

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        # Initialize an empty list to hold expenses
        self.expenses = []

        # Create input fields for expense entry
        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.pack(pady=5)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack(pady=5)

        self.description_label = tk.Label(root, text="Description:")
        self.description_label.pack(pady=5)
        self.description_entry = tk.Entry(root)
        self.description_entry.pack(pady=5)

        # Create a button to add expense
        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.pack(pady=20)

        # Create a button to show monthly summary
        self.summary_button = tk.Button(root, text="Show Monthly Summary", command=self.show_summary)
        self.summary_button.pack(pady=20)

        # Create a label to display the total expenses
        self.total_label = tk.Label(root, text="Total Expenses: $0.00")
        self.total_label.pack(pady=20)

    def add_expense(self):
        """Add an expense to the list."""
        try:
            amount = float(self.amount_entry.get())
            description = self.description_entry.get()
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            self.expenses.append({'amount': amount, 'description': description, 'date': date})

            # Clear the entry fields
            self.amount_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)

            # Update the total expenses display
            self.update_total_expenses()
            messagebox.showinfo("Success", "Expense added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def update_total_expenses(self):
        """Update the total expenses label."""
        total = sum(expense['amount'] for expense in self.expenses)
        self.total_label.config(text=f"Total Expenses: ${total:.2f}")

    def show_summary(self):
        """Show a summary of expenses for the current month."""
        current_month = datetime.datetime.now().strftime("%Y-%m")
        monthly_expenses = [expense for expense in self.expenses if expense['date'].startswith(current_month)]

        if not monthly_expenses:
            messagebox.showinfo("Monthly Summary", "No expenses recorded for this month.")
            return

        summary = "\n".join(f"{expense['date']} - {expense['description']}: ${expense['amount']:.2f}" for expense in monthly_expenses)
        total_monthly = sum(expense['amount'] for expense in monthly_expenses)
        summary += f"\n\nTotal for {current_month}: ${total_monthly:.2f}"

        messagebox.showinfo("Monthly Summary", summary)

# Create the main window
root = tk.Tk()
app = ExpenseTracker(root)

# Start the Tkinter main loop
root.mainloop()