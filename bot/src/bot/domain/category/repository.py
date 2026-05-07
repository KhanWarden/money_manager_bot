from abc import ABC, abstractmethod

from bot.domain.category import Category
from bot.domain.shared import EntityId


class ICategoryRepository(ABC):
    @abstractmethod
    def get_by_name(self, category_id: EntityId) -> Category | None:
        pass

    @abstractmethod
    def save(self, name: str) -> None:
        pass
