from dataclasses import dataclass
from datetime import datetime

from bot.domain.shared import Money, EntityId


@dataclass
class Expense:
    id: EntityId
    user_id: EntityId
    amount: Money
    category_id: EntityId
    created_at: datetime
