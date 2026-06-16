from zoneinfo import ZoneInfo

from domain.shared import EntityId
from domain.user import IUserRepository, User
from domain.user.exceptions import UserAlreadyExistsException


class CreateUserUseCase:
    def __init__(self, user_repository: IUserRepository) -> None:
        self._users = user_repository

    async def execute(self, telegram_id: int, timezone: ZoneInfo) -> None:
        if await self._users.get_by_telegram_id(telegram_id):
            raise UserAlreadyExistsException

        user = User(
            id=EntityId.generate(),
            telegram_id=telegram_id,
            timezone=timezone,
        )
        await self._users.save(user)
