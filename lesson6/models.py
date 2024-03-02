from pydantic import BaseModel


class UserIn(BaseModel):
    name: str
    email: str
    password: str


class User(BaseModel):
    id: int
    name: str
    email: str
    password_hash: str


class OrderIn(BaseModel):
    user_id: int
    product_id: int
    order_date: str
    status: str


class Order(BaseModel):
    id: int
    user_id: int
    product_id: int
    order_date: str
    status: str


class ProductIn(BaseModel):
    name: str
    description: str
    price: float


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
