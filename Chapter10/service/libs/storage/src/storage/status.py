"""Abstractions for the status of a delivery."""
from typing import Union


class DispatchedOrder:
    """An order that was just created and notified to start its delivery."""

    status = "dispatched"

    def __init__(self, when):
        self._when = when

    def message(self) -> dict:
        return {
            "status": self.status,
            "msg": "Order was dispatched on {0}".format(
                self._when.isoformat()
            ),
        }


class OrderInTransit:
    """An order that is currently being sent to the customer."""

    status = "in transit"

    def __init__(self, current_location):
        self._current_location = current_location

    def message(self) -> dict:
        return {
            "status": self.status,
            "msg": "The order is in progress (current location: {})".format(
                self._current_location
            ),
        }


class OrderDelivered:
    """An order that was already delivered to the customer."""

    status = "delivered"

    def __init__(self, delivered_at):
        self._delivered_at = delivered_at

    def message(self) -> dict:
        return {
            "status": self.status,
            "msg": "Order delivered on {0}".format(
                self._delivered_at.isoformat()
            ),
        }


class DeliveryOrder:
    def __init__(
        self,
        delivery_id: str,
        status: Union[DispatchedOrder, OrderInTransit, OrderDelivered],
    ) -> None:
        self._delivery_id = delivery_id
        self._status = status

    def message(self) -> dict:
        return {"id": self._delivery_id, **self._status.message()}
