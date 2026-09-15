from fastapi import FastAPI, HTTPException
from schemas import CustomerCreate
from crud import (
    create_customer,
    get_customers,
    get_customer_by_id,
    update_customer,
    delete_customer
)

app = FastAPI()


@app.post("/customers")
def add_customer(customer: CustomerCreate):
    create_customer(
        customer.name,
        customer.email,
        customer.phone,
        customer.city,
        customer.age
    )

    return {
        "message": "Customer created successfully"
    }


@app.get("/customers")
def read_customers():
    customers = get_customers()

    return customers


@app.get("/customers/{customer_id}")
def read_customer(customer_id: int):
    customer = get_customer_by_id(customer_id)

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer


@app.put("/customers/{customer_id}")
def update_customer_data(customer_id: int, customer: CustomerCreate):
    customer_exists = get_customer_by_id(customer_id)

    if customer_exists is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    update_customer(
        customer_id,
        customer.name,
        customer.phone,
        customer.city
    )

    return {
        "message": "Customer updated successfully"
    }


@app.delete("/customers/{customer_id}")
def remove_customer(customer_id: int):
    deleted = delete_customer(customer_id)

    if deleted == 0:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return {
        "message": "Customer deleted successfully"
    }