from typing import Any
from fastapi import APIRouter, Depends

from ..auth import Authentication, Claims

from ..service import OrdersService
from ..beans import get_orders_service
from ..model import CreateOrder, CaptureOrder, PaypalCreateOrderRequestBody

ordersRouter = APIRouter(tags=["Orders"], prefix="/orders")

@ordersRouter.post("", operation_id="create_order", response_model=PaypalCreateOrderRequestBody)
async def create_order(
    payload: CreateOrder,
    auth: Claims = Depends(Authentication),
    orderService: OrdersService = Depends(get_orders_service)
) -> PaypalCreateOrderRequestBody:
    """Creates a new order"""
    return await orderService.new(payload)

@ordersRouter.put("/{orderId}/capture", operation_id="capture", response_model=dict[str, Any])
async def capture(
    orderId: str,
    payload: CaptureOrder,
    auth: Claims = Depends(Authentication),
    orderService: OrdersService = Depends(get_orders_service)
) -> dict[str, Any]:
    return await orderService.capture(orderId, payload)
