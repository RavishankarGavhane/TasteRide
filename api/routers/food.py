from fastapi import APIRouter, HTTPException
from typing import List, Optional
from datetime import date

router = APIRouter()

# Example data (for demonstration purposes)
food_orders = [
    {"id": 1, "employee": "Ravi", "meal": "Breakfast", "status": "DELIVERED", "date": "2024-04-01"},
    {"id": 2, "employee": "Shona", "meal": "Lunch", "status": "DELIVERED", "date": "2024-04-01"},
    {"id": 3, "employee": "Ram", "meal": "Dinner", "status": "PENDING", "date": "2024-04-01"},
    {"id": 4, "employee": "Eva", "meal": "Breakfast", "status": "CANCELED", "date": "2024-04-02"},
    {"id": 5, "employee": "Kayara", "meal": "Lunch", "status": "DELIVERED", "date": "2024-04-02"},
    {"id": 6, "employee": "Shita", "meal": "Dinner", "status": "DELIVERED", "date": "2024-04-02"},
]

# Function to calculate the total fine for an employee
def calculate_total_fine(employee: str):
    fine_amount = sum(100 if order["status"] == "PENDING" else 0 for order in food_orders if order["employee"] == employee)
    return fine_amount

# Endpoint to get the food orders for an employee
@router.get("/food_orders/{employee}", response_model=List[dict])
async def get_food_orders(employee: str):
    return [order for order in food_orders if order["employee"] == employee]

# Endpoint to get the total fine for an employee
@router.get("/total_fine/{employee}")
async def get_total_fine(employee: str):
    return {"total_fine": calculate_total_fine(employee)}

# Endpoint to get the total fine for all employees
@router.get("/total_fine")
async def get_total_fine_all():
    employees = set(order["employee"] for order in food_orders)
    total_fine_all = sum(calculate_total_fine(employee) for employee in employees)
    return {"total_fine": total_fine_all}
