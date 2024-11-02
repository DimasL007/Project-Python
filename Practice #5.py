class FinanceBot:
    def __init__(self):
        self.income = 0
        self.expenses = []
        self.budget = 0

    def add_income(self, amount):
        self.income += amount
        print(f"Доход {amount} грн додано. Загальний доход: {self.income} грн.")

    def add_expense(self, description, amount):
        self.expenses.append({'description': description, 'amount': amount})
        print(f"Витрата '{description}' на суму {amount} грн додана.")

    def set_budget(self, amount):
        self.budget = amount
        print(f"Бюджет встановлено на рівні {self.budget} грн.")

    def show_statistics(self):
        total_expenses = sum(expense['amount'] for expense in self.expenses)
        balance = self.income - total_expenses
        print("\n==== Статистика ====")
        print(f"Загальний доход: {self.income} грн")
        print(f"Загальні витрати: {total_expenses} грн")
        print(f"Баланс: {balance} грн")
        if total_expenses > self.budget:
            print("Увага: Ви перевищили бюджет!")
        elif balance < 0:
            print("Попередження: Ваші витрати перевищують доходи!")
        else:
            print("Все в порядку: Ви в межах бюджету.")

    def savings_tips(self):
        print("\n==== Поради щодо економії ====")
        if self.income == 0:
            print("Рекомендація: Додайте джерело доходу.")
        if len(self.expenses) == 0:
            print("Рекомендація: Необхідно додати витрати для аналізу.")
        total_expenses = sum(expense['amount'] for expense in self.expenses)
        if total_expenses > self.budget:
            print("Рекомендація: Скоротіть витрати або збільште бюджет.")
        else:
            print("Рекомендація: Відкладіть частину доходів на заощадження.")

# Приклад використання бота
bot = FinanceBot()

# Додаємо доходи та витрати
bot.add_income(10000)
bot.add_expense("Їжа", 3000)
bot.add_expense("Транспорт", 500)
bot.add_expense("Розваги", 1000)

# Встановлення бюджету
bot.set_budget(5000)

# Показування статистики
bot.show_statistics()

# Поради щодо економії
bot.savings_tips()