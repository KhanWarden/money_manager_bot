from abc import ABC, abstractmethod

from bot.domain.user import User


class IUserRepository(ABC):
    @abstractmethod
    async def save(self, user: User) -> None:
        pass

    @abstractmethod
    async def get_by_telegram_id(self, telegram_id: int) -> User | None:
        pass
