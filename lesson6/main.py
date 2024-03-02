from typing import List
from fastapi import FastAPI
from models import User, UserIn, Product, ProductIn, Order, OrderIn
from db_models import database, users, orders, products
from werkzeug.security import generate_password_hash

app = FastAPI()


@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(name=user.name, email=user.email,
                                  password_hash=generate_password_hash(
                                      user.password,  method='pbkdf2:sha256'))
    last_record_id = await database.execute(query)
    return {**user.model_dump(), "id": last_record_id}


@app.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserIn):
    query = users.update().where(users.c.id == user_id).values(
        password_hash=generate_password_hash(
            user.password,  method='pbkdf2:sha256'))
    await database.execute(query)
    return await read_user(user_id)


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {"status": "Product deleted"}


@app.post("/products/", response_model=Product)
async def create_product(product: ProductIn):
    query = products.insert().values(
        name=product.name, description=product.description, price=product.price)
    last_record_id = await database.execute(query)
    return {**product.model_dump(), "id": last_record_id}


@app.get("/products/", response_model=List[Product])
async def read_products():
    query = products.select()
    return await database.fetch_all(query)


@app.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query)


@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, product: ProductIn):
    query = products.update().where(products.c.id == product_id).values(
        name=product.name, description=product.description, price=product.price)
    await database.execute(query)
    return await read_product(product_id)


@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {"status": "Product deleted"}


@app.post("/orders/", response_model=Order)
async def create_order(order: OrderIn):
    query = orders.insert().values(user_id=order.user_id, product_id=order.product_id,
                                   order_date=order.order_date, status=order.status)
    last_record_id = await database.execute(query)
    return {**order.model_dump(), "id": last_record_id}


@app.get("/orders/", response_model=List[Order])
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)


@app.get("/orders/{order_id}", response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@app.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(user_id=order.user_id,
                                                                  product_id=order.product_id, order_date=order.order_date, status=order.status)
    await database.execute(query)
    return await read_order(order_id)


@app.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {"status": "Order deleted"}
