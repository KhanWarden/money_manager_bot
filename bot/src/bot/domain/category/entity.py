from dataclasses import dataclass

from bot.domain.shared import EntityId


@dataclass
class Category:
    id: EntityId
    user_id: EntityId
    name: str
    is_active: bool = True

    def activate(self) -> None:
        self.is_active = True

    def deactivate(self) -> None:
        self.is_active = False
