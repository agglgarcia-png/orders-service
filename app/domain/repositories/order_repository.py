from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.entities.order import Order


class OrderRepository(ABC):

    @abstractmethod
    def save(self, order: Order) -> None:
        """
        Guarda una nueva orden.
        """

    @abstractmethod
    def get_by_id(self, order_id: UUID) -> Order | None:
        """
        Obtiene una orden por su identificador.
        """

    @abstractmethod
    def update(self, order: Order) -> None:
        """
        Actualiza una orden existente.
        """

    @abstractmethod
    def delete(self, order_id: UUID) -> None:
        """
        Elimina una orden.
        """
