from domain.account import IAccountRepository, AccountKind, Account
from domain.account.exceptions import AccountAlreadyExistsException
from domain.shared import Money, EntityId
from domain.user import IUserRepository


class CreateAccountUseCase:
    def __init__(
        self,
        user_repository: IUserRepository,
        account_repository: IAccountRepository,
    ) -> None:
        self._users = user_repository
        self._accounts = account_repository

    async def execute(
        self,
        telegram_id: int,
        name: str,
        amount: Money,
        account_kind: AccountKind,
    ) -> None:
        user = await self._users.get_by_telegram_id(telegram_id)
        if await self._accounts.get_by_name(user_id=user.id, name=name):
            raise AccountAlreadyExistsException()

        account = Account(
            id=EntityId.generate(),
            user_id=user.id,
            name=name,
            amount=amount,
            account_kind=account_kind,
        )
        await self._accounts.save(account)
