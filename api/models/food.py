from typing import Optional
from pydantic import BaseModel
from datetime import date

class FoodOrder(BaseModel):
    id: int
    name: str
    status: str
    cancel: Optional[bool]
    price: Optional[float]
    date: date
    fine_amount: Optional[int]
