from typing import Any

from ..model.order import *
from ..model.paypal import *
from .paypal import PaypalService


class OrdersService:
    paypalService: PaypalService

    def __init__(self, paypalService: PaypalService):
        self.paypalService = paypalService

    async def new(self, payload: CreateOrder) -> PaypalCreateOrderRequestBody:
        return PaypalCreateOrderRequestBody(
            purchase_units=[PaypalPurchaseUnit(amount=PaypalAmount(value=10), invoice_id="test")]
        )

    async def capture(self,orderId: str, payload: CaptureOrder) -> dict[str, Any]:
        capture = await self.paypalService.capture_order(orderId)
        return capture
