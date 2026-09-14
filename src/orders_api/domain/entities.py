from dataclasses import dataclass

from orders_api.domain.exceptions import InvalidOrderError


@dataclass
class Order:
    id: int
    customer: str
    amount: float

    def validate(self) -> None:

        if not self.customer:
            raise InvalidOrderError(
                "Customer is required"
            )

        if self.amount <= 0:
            raise InvalidOrderError(
                "Amount must be greater than zero"
            )
            