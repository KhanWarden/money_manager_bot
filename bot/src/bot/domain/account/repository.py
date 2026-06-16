from abc import ABC, abstractmethod

from bot.domain.account import Account
from bot.domain.shared import EntityId


class IAccountRepository(ABC):
    @abstractmethod
    async def save(self, account: Account) -> None:
        pass

    @abstractmethod
    async def get_by_id(self, account_id: EntityId) -> Account | None:
        pass

    @abstractmethod
    async def get_by_user(self, user_id: int) -> list[Account] | None:
        pass

    @abstractmethod
    async def get_by_name(self, user_id: EntityId, name: str):
        pass
