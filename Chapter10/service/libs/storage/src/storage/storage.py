"""Adapter from the low level (BD) to high level objects."""

from .client import DBClient
from .converters import build_from_row
from .status import DeliveryOrder


class DeliveryStatusQuery:
    def __init__(self, delivery_id: int, dbclient: DBClient) -> None:
        self._delivery_id = delivery_id
        self._client = dbclient

    async def get(self) -> DeliveryOrder:
        """Get the current status for this delivery."""
        results = await self._run_query()
        return build_from_row(self._delivery_id, results)

    async def _run_query(self):
        return await self._client.fetchrow(
            """
            SELECT status, d.dispatched_at, t.location, f.delivered_at
            FROM delivery_order_status as dos
                LEFT JOIN dispatched as d ON (dos.delivery_id = d.delivery_id)
                LEFT JOIN in_transit as t ON (dos.delivery_id = t.delivery_id)
                LEFT JOIN finished as f ON (dos.delivery_id = f.delivery_id)
            WHERE dos.delivery_id = $1
        """,
            self._delivery_id,
        )
