from domain.category import ICategoryRepository, Category
from domain.category.exceptions import CategoryAlreadyExistsException
from domain.shared import EntityId
from domain.user import IUserRepository


class CreateCategoryUseCase:
    def __init__(
        self, user_repository: IUserRepository, category_repository: ICategoryRepository
    ) -> None:
        self._users = user_repository
        self._categories = category_repository

    async def execute(
        self,
        telegram_id: int,
        name: str,
    ) -> None:
        user = await self._users.get_by_telegram_id(telegram_id)
        if await self._categories.get_by_name(user_id=user.id, name=name):
            raise CategoryAlreadyExistsException()

        category = Category(
            id=EntityId.generate(),
            user_id=user.id,
            name=name,
        )
        await self._categories.save(category)
