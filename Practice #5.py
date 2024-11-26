class FinanceBot:  # Клас для управління фінансами
    def __init__(self):  # Ініціалізація атрибутів об'єкта
        self.income = 0  # Загальний доход
        self.expenses = []  # Список витрат (з описом і сумою)
        self.budget = 0  # Бюджет

    def add_income(self, amount):  # Метод для додавання доходу
        self.income += amount  # Додає суму до загального доходу
        print(f"Доход {amount} грн додано. Загальний доход: {self.income} грн.")

    def add_expense(self, description, amount):  # Метод для додавання витрат
        self.expenses.append({'description': description, 'amount': amount})  # Додає витрати у список
        print(f"Витрата '{description}' на суму {amount} грн додана.")

    def set_budget(self, amount):  # Метод для встановлення бюджету
        self.budget = amount  # Встановлює новий бюджет
        print(f"Бюджет встановлено на рівні {self.budget} грн.")

    def show_statistics(self):  # Метод для відображення статистики фінансів
        total_expenses = sum(expense['amount'] for expense in self.expenses)  # Обчислює загальні витрати
        balance = self.income - total_expenses  # Розраховує баланс (доходи мінус витрати)
        print("\n==== Статистика ====")
        print(f"Загальний доход: {self.income} грн")
        print(f"Загальні витрати: {total_expenses} грн")
        print(f"Баланс: {balance} грн")
        if total_expenses > self.budget:  # Перевіряє, чи витрати перевищують бюджет
            print("Увага: Ви перевищили бюджет!")
        elif balance < 0:  # Перевіряє, чи витрати перевищують доходи
            print("Попередження: Ваші витрати перевищують доходи!")
        else:
            print("Все в порядку: Ви в межах бюджету.")

    def savings_tips(self):  # Метод для надання порад щодо економії
        print("\n==== Поради щодо економії ====")
        if self.income == 0:  # Якщо доходи нульові
            print("Рекомендація: Додайте джерело доходу.")
        if len(self.expenses) == 0:  # Якщо витрати не додані
            print("Рекомендація: Необхідно додати витрати для аналізу.")
        total_expenses = sum(expense['amount'] for expense in self.expenses)  # Обчислює загальні витрати
        if total_expenses > self.budget:  # Якщо витрати перевищують бюджет
            print("Рекомендація: Скоротіть витрати або збільште бюджет.")
        else:  # Якщо все в порядку
            print("Рекомендація: Відкладіть частину доходів на заощадження.")

# Приклад використання бота
bot = FinanceBot()  # Створюємо екземпляр класу FinanceBot

# Додаємо доходи
bot.add_income(10000)  # Додаємо доход 10,000 грн

# Додаємо витрати
bot.add_expense("Їжа", 3000)  # Витрати на їжу 3000 грн
bot.add_expense("Транспорт", 500)  # Витрати на транспорт 500 грн
bot.add_expense("Розваги", 1000)  # Витрати на розваги 1000 грн

# Встановлення бюджету
bot.set_budget(5000)  # Встановлюємо бюджет на рівні 5000 грн

# Показуємо статистику
bot.show_statistics()  # Відображаємо доходи, витрати, баланс і статус бюджету

# Показуємо поради щодо економії
bot.savings_tips()  # Виводимо рекомендації для покращення фінансового стану