class OrderError(Exception):
    """Excepción base del dominio."""


class CustomerRequiredError(OrderError):
    """El cliente es obligatorio."""


class InvalidOrderAmountError(OrderError):
    """El monto debe ser mayor que cero."""


class InvalidOrderStatusTransitionError(OrderError):
    """Transición de estado no permitida."""


class OrderNotFoundError(OrderError):
    """La orden no existe."""