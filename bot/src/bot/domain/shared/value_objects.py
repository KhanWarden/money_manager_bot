from dataclasses import dataclass
from uuid import UUID, uuid4
from decimal import Decimal


@dataclass
class EntityId:
    value: UUID

    @classmethod
    def generate(cls) -> "EntityId":
        return cls(value=uuid4())

    @classmethod
    def from_string(cls, value: str) -> "EntityId":
        return cls(value=UUID(value))


@dataclass
class Money:
    amount: Decimal

    def __post_init__(self) -> None:
        if self.amount < Decimal("0"):
            raise ValueError("Amount cannot be less than zero")

    def __add__(self, other: "Money") -> "Money":
        return Money(amount=self.amount + other.amount)

    def __sub__(self, other: "Money") -> "Money":
        return Money(amount=self.amount - other.amount)
