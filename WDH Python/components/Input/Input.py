import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import random, os, json


class Input(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.expenditures = []
        self.income = []
        self.transactions = {"Expenditures": [], "Income": []}
        self.overview_state = tk.StringVar(
            value=f"Expenditures: {sum(self.expenditures)}, Income: {sum(self.income)}, Saldo: {self.calc_saldo()}"
        )

        self.overview_label = ttk.Label(self, textvariable=self.overview_state)
        self.overview_label.pack()

        # Userinputframe
        self.input_frame = ttk.Frame(self)
        self.input_frame.pack()

        # Amount
        self.amount_frame = ttk.Frame(self.input_frame)
        self.amount_frame.pack()
        self.amount_label = ttk.Label(self.amount_frame, text="Amount: ")
        self.amount_label.pack(side="left")
        self.amount_input = ttk.Entry(self.amount_frame)
        self.amount_input.pack(side="right")

        # Description
        self.description_frame = ttk.Frame(self.input_frame)
        self.description_frame.pack()
        self.description_label = ttk.Label(self.description_frame, text="Description: ")
        self.description_label.pack(side="left")
        self.description_input = ttk.Entry(self.description_frame)
        self.description_input.pack(side="right")

        # Category
        self.category_frame = ttk.Frame(self.input_frame)
        self.category_frame.pack()
        self.category_label = ttk.Label(self.category_frame, text="Category: ")
        self.category_label.pack(side="left")
        self.category_input = ttk.Entry(self.category_frame)
        self.category_input.pack(side="right")

        # Buttons
        self.button_expenditures = ttk.Button(
            self, text="Add as expenditure", command=self.add_expenditure
        )
        self.button_expenditures.pack()

        self.button_income = ttk.Button(
            self, text="Add as income", command=self.add_income
        )
        self.button_income.pack()

        # Transactions
        self.transactions_frame = ttk.Frame(self)
        self.transactions_frame.pack(expand=True, fill="x")

        self.listbox = tk.Listbox(self.transactions_frame)
        self.listbox.pack(fill=tk.X, expand=True, padx=4, pady=4, ipadx=4, ipady=4)

        self.create_txt = ttk.Button(
            self, text="Save transactions", command=self.create_txt_file
        )
        self.create_txt.pack()

    def create_txt_file(self):
        # Construct the full path to the file in the project root
        file_path_in_root = os.path.join(self.master.root_path, "transactions.txt")

        try:
            with open(os.path.abspath(file_path_in_root), "w") as file:
                transactions_json = json.dumps(self.transactions)
                file.write(transactions_json)

            messagebox.showinfo("Success", "The file has been created.")

        except IOError as e:
            print(f"Error creating file: {e}")

    def add_new_transaction(self, transaction):
        now = datetime.now()
        new_item = {
            "id": random.random(),
            "description": transaction[2],
            "category": transaction[3],
            "value": transaction[1],
            "timestamp": now.strftime("%d/%m/%Y %H:%M"),
        }

        self.transactions[transaction[0]].append(new_item)

        self.listbox.insert(
            tk.END,
            f"{"Expenditure" if transaction[0] == "Expenditures" else "Income"}: {new_item['value']}, Category: {new_item['category']}, Date: {new_item['timestamp']}",
        )

    def add_expenditure(self):
        try:
            expenditure = float(self.amount_input.get())
            self.expenditures.append(expenditure)
            self.overview_state.set(
                value=f"Expenditures: {sum(self.expenditures)}, Income: {sum(self.income)}, Saldo: {self.calc_saldo()}"
            )
            self.add_new_transaction(
                (
                    "Expenditures",
                    expenditure,
                    self.description_input.get(),
                    self.category_input.get(),
                )
            )

            self.amount_input.delete(0, tk.END)
            self.description_input.delete(0, tk.END)
            self.category_input.delete(0, tk.END)

            messagebox.showinfo("Success", f"Added {expenditure}.")

        except ValueError as e:
            messagebox.showerror("Valueerror", "Value has to be a number.")

    def add_income(self):
        try:
            income = float(self.amount_input.get())
            self.income.append(income)
            self.overview_state.set(
                value=f"Expenditures: {sum(self.expenditures)}, Income: {sum(self.income)}, Saldo: {self.calc_saldo()}"
            )
            self.add_new_transaction(
                (
                    "Income",
                    income,
                    self.description_input.get(),
                    self.category_input.get(),
                )
            )

            self.amount_input.delete(0, tk.END)
            self.description_input.delete(0, tk.END)
            self.category_input.delete(0, tk.END)

            messagebox.showinfo("Success", f"Added {income}.")

        except ValueError as e:
            messagebox.showerror("Valueerror", "Value has to be a number.")

    def calc_saldo(self):
        return sum(self.income) - sum(self.expenditures)
