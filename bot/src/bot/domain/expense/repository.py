from abc import ABC, abstractmethod
from datetime import datetime

from bot.domain.expense import Expense
from bot.domain.shared import Money, EntityId


class IExpenseRepository(ABC):
    @abstractmethod
    async def save(self, expense: Expense) -> None:
        pass

    @abstractmethod
    async def get_by_period(
        self,
        period_start: datetime,
        period_end: datetime,
    ) -> list[Expense]:
        pass

    @abstractmethod
    async def get_by_category(
        self,
        category_id: EntityId,
        period_start: datetime,
        period_end: datetime,
    ) -> list[Expense]:
        pass
