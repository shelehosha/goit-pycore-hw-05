import re
from typing import Callable

def generator_numbers(text: str):
    """ Генератор, який повертає всі дійсні числа з тексту."""
    numbers = re.findall(r'\b\d+\.\d+\b', text)
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable):
    """ Обчислює загальну суму чисел у тексті, використовуючи generator_numbers."""
    total = sum(func(text))
    return total
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")