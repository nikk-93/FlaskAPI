from datetime import datetime
import databases
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
import sqlalchemy

DATABASE_URL = "sqlite:///mydatabase.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


users = sqlalchemy.Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True),
    Column("email", String, unique=True, index=True),
    Column("password_hash", String))

products = sqlalchemy.Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True),
    Column("description", String, index=True),
    Column("price", Integer))

orders = sqlalchemy.Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("user_id", Integer, ForeignKey("users.id"), index=True),
    Column("product_id", Integer, ForeignKey("products.id"), index=True),
    Column("order_date", DateTime, default=datetime.utcnow),
    Column("status", String))


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)
