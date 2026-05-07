from dataclasses import dataclass
from decimal import Decimal

from bot.domain.account import AccountKind
from bot.domain.shared import EntityId, Money


@dataclass
class Account:
    id: EntityId
    user_id: EntityId
    name: str
    amount: Money
    account_kind: AccountKind
    is_active: bool = True

    def add_money(self, amount: Money) -> None:
        self.amount += amount

    def subtract_money(self, amount: Money) -> None:
        self.amount -= amount

    def activate(self) -> None:
        self.is_active = True

    def deactivate(self) -> None:
        self.is_active = False
