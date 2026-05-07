from abc import ABC, abstractmethod
from datetime import datetime

from bot.domain.expense import Expense
from bot.domain.shared import Money, EntityId


class IExpenseRepository(ABC):
    @abstractmethod
    def save(
        self,
        amount: Money,
        category_id: EntityId,
    ) -> None:
        pass

    @abstractmethod
    def get(
        self,
        period_start: datetime,
        period_end: datetime,
    ) -> list[Expense]:
        pass

    @abstractmethod
    def get_by_category(
        self,
        category_id: EntityId,
        period_start: datetime,
        period_end: datetime,
    ) -> list[Expense]:
        pass
