import tkinter as tk
from tkinter import messagebox, font

class BudgetApp:
    def __init__(self):
        self.budget_limit = 0
        self.expenses = []

    def set_budget_limit(self, limit):
        self.budget_limit = limit

    def add_expense(self, amount):
        self.expenses.append(amount)

    def get_total_expenses(self):
        return sum(self.expenses)

    def get_remaining_budget(self):
        return self.budget_limit - self.get_total_expenses()

    def analyze_expenses(self):
        return {
            "total_expenses": self.get_total_expenses(),
            "remaining_budget": self.get_remaining_budget(),
            "expenses": self.expenses
        }

class BudgetAppUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Бюджетное планирование")
        self.master.geometry("400x500")  # Увеличиваем размер окна
        self.master.configure(bg="#3A8EBA")  # Установка цвета фона

        # Настройка шрифтов
        self.title_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.label_font = font.Font(family="Helvetica", size=12)
        self.button_font = font.Font(family="Helvetica", size=12)

        self.budget_app = BudgetApp()

        # Заголовок
        self.title_label = tk.Label(master, text="Бюджетное планирование", font=self.title_font, bg="#3A8EBA", fg="white")
        self.title_label.pack(anchor='w', padx=10, pady=10)

        # Ввод лимита бюджета
        self.limit_label = tk.Label(master, text="Установите лимит бюджета:", font=self.label_font, bg="#3A8EBA", fg="white")
        self.limit_label.pack(anchor='w', padx=10, pady=5)

        self.limit_entry = tk.Entry(master, font=self.label_font)
        self.limit_entry.pack(anchor='w', padx=10, pady=5)

        self.set_limit_button = tk.Button(master, text="Установить лимит", command=self.set_budget_limit, font=self.button_font)
        self.set_limit_button.pack(anchor='w', padx=10, pady=10, fill='x')

        # Ввод расходов
        self.expense_label = tk.Label(master, text="Добавьте расход:", font=self.label_font, bg="#3A8EBA", fg="white")
        self.expense_label.pack(anchor='w', padx=10, pady=5)

        self.expense_entry = tk.Entry(master, font=self.label_font)
        self.expense_entry.pack(anchor='w', padx=10, pady=5)

        self.add_expense_button = tk.Button(master, text="Добавить расход", command=self.add_expense, font=self.button_font)
        self.add_expense_button.pack(anchor='w', padx=10, pady=10, fill='x')

        # Кнопка для анализа
        self.analyze_button = tk.Button(master, text="Анализировать расходы", command=self.analyze_expenses, font=self.button_font)
        self.analyze_button.pack(anchor='w', padx=10, pady=10, fill='x')

        # Поле для отображения информации
        self.result_label = tk.Label(master, text="", font=self.label_font, bg="#3A8EBA", fg="white")
        self.result_label.pack(anchor='w', padx=10, pady=10)

    def set_budget_limit(self):
        try:
            limit = float(self.limit_entry.get())
            self.budget_app.set_budget_limit(limit)
            messagebox.showinfo("Информация", f"Лимит бюджета установлен на {limit}!")
            self.limit_entry.delete(0, tk.END)  # Очистка поля после ввода
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное число.")

    def add_expense(self):
        try:
            expense = float(self.expense_entry.get())
            self.budget_app.add_expense(expense)
            messagebox.showinfo("Информация", f"Расход {expense} добавлен!")
            self.expense_entry.delete(0, tk.END)  # Очистка поля после ввода
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное число.")

    def analyze_expenses(self):
        analysis = self.budget_app.analyze_expenses()
        total_expenses = analysis["total_expenses"]
        remaining_budget = analysis["remaining_budget"]
        expenses = analysis["expenses"]

        result_text = (f"Общие расходы: {total_expenses}\n"
                       f"Оставшийся бюджет: {remaining_budget}\n"
                       f"Список расходов: {expenses}")
        self.result_label.config(text=result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetAppUI(root)
    root.mainloop()
