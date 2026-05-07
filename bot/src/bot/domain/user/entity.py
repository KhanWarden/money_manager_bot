from dataclasses import dataclass
from zoneinfo import ZoneInfo

from bot.domain.shared import EntityId


@dataclass
class User:
    id: EntityId
    telegram_id: int
    timezone: ZoneInfo

    def change_timezone(self, new_timezone: ZoneInfo) -> None:
        self.timezone = new_timezone
