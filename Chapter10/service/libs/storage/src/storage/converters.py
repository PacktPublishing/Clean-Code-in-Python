"""Convert the row resulting from a query to the Entities object."""
from .status import (DeliveryOrder, DispatchedOrder, OrderDelivered,
                     OrderInTransit)


def build_dispatched(row):
    return DispatchedOrder(row.dispatched_at)


def build_in_transit(row):
    return OrderInTransit(row.location)


def build_delivered(row):
    return OrderDelivered(row.delivered_at)


_BUILD_MAPPING = {
    "d": build_dispatched,
    "t": build_in_transit,
    "f": build_delivered,
}


class WrappedRow:
    def __init__(self, row):
        self._row = row

    def __getattr__(self, attrname):
        return self._row[attrname]


class OrderNotFoundError(Exception):
    """The requested order does not appear listed."""


def build_from_row(delivery_id, row):
    if row is None:
        raise OrderNotFoundError(f"{delivery_id} was not found")

    row = WrappedRow(row)
    status_builder = _BUILD_MAPPING[row.status]
    status = status_builder(row)
    return DeliveryOrder(delivery_id, status)
