import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import random, os, json


class Input(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

        self.expenditures = []
        self.income = []
        self.transactions = {"Expenditures": [], "Income": []}
        self.overview_state = tk.StringVar(
            value=f"Expenditures: {sum(self.expenditures)}, Income: {sum(self.income)}, Saldo: {self.calc_saldo()}"
        )

        self.overview_label = ttk.Label(self, textvariable=self.overview_state)
        self.overview_label.pack(anchor="w", pady=4, padx=4)

        # Topframe
        self.top_frame = ttk.Frame(self)
        self.top_frame.pack()

        # Userinputframe
        self.input_frame = ttk.Frame(self.top_frame)
        self.input_frame.pack(side="left")

        # Amount
        self.amount_frame = ttk.Frame(self.input_frame, padding=4)
        self.amount_frame.pack(expand=True, fill="x")
        self.amount_label = ttk.Label(self.amount_frame, text="Amount: ")
        self.amount_label.pack(side="left")
        self.amount_input = ttk.Entry(self.amount_frame)
        self.amount_input.pack(side="right")

        # Description
        self.description_frame = ttk.Frame(self.input_frame, padding=4)
        self.description_frame.pack(expand=True, fill="x")
        self.description_label = ttk.Label(self.description_frame, text="Description: ")
        self.description_label.pack(side="left")
        self.description_input = ttk.Entry(self.description_frame)
        self.description_input.pack(side="right")

        # Category
        self.category_frame = ttk.Frame(self.input_frame, padding=4)
        self.category_frame.pack(expand=True, fill="x")
        self.category_label = ttk.Label(self.category_frame, text="Category: ")
        self.category_label.pack(side="left")
        self.category_input = ttk.Entry(self.category_frame)
        self.category_input.pack(side="right")

        # Buttons
        self.button_frame = ttk.Frame(self.top_frame, padding=(32, 0, 0, 0))
        self.button_frame.pack(side="right")
        self.button_expenditures = ttk.Button(
            self.button_frame,
            text="Add as expenditure",
            command=self.add_expenditure,
            cursor="hand2",
        )
        self.button_expenditures.pack(expand=True, fill="x", padx=4, pady=4)
        self.button_income = ttk.Button(
            self.button_frame,
            text="Add as income",
            command=self.add_income,
            cursor="hand2",
        )
        self.button_income.pack(expand=True, fill="x", padx=4, pady=4)

        # Bottomframe
        self.bottom_frame = ttk.Frame(self)
        self.bottom_frame.pack()

        # Transactions
        self.transactions_frame = ttk.Frame(self.bottom_frame)
        self.transactions_frame.pack(expand=True, fill="x", padx=4, pady=4)

        self.scrollbar = tk.Scrollbar(self.transactions_frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create the Listbox and link both scrollbars
        self.listbox = tk.Listbox(
            self.transactions_frame,
            yscrollcommand=self.scrollbar.set,  # Link vertical scrollbar
            width=80,
            font=("16"),
            justify="center",
        )
        self.listbox.pack(fill=tk.X, expand=True, padx=4, pady=4)

        self.create_txt = ttk.Button(
            self.bottom_frame,
            text="Save",
            command=self.create_txt_file,
            cursor="hand2",
        )
        self.create_txt.pack(pady=4)

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
            f"{"Expenditure" if transaction[0] == "Expenditures" else "Income"}: {new_item['value']}, Description: {new_item['description']}, Category: {new_item['category']}, Date: {new_item['timestamp']}",
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
