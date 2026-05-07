from enum import Enum


class AccountKind(Enum):
    PAYMENT = 1  # Основной для платежей
    SAVINGS = 2  # Накопительный / Депозит
    CREDIT = 3  # Кредитная карта
    INVESTMENT = 4  # Инвестиционный
