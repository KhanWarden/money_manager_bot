from dataclasses import dataclass

from bot.domain.shared import Money, EntityId


@dataclass
class Expense:
    id: EntityId
    amount: Money
    category_id: EntityId
