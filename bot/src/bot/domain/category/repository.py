from abc import ABC, abstractmethod

from bot.domain.category import Category
from bot.domain.shared import EntityId


class ICategoryRepository(ABC):
    @abstractmethod
    async def get_by_name(
        self,
        user_id: EntityId,
        name: str,
    ) -> Category | None:
        pass

    @abstractmethod
    async def save(self, category: Category) -> None:
        pass
