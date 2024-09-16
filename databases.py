from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, Float

# CREATE DATABASE
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# CONFIGURE TABLES

# Create a User table for all your registered users
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(100))


class Property(db.Model):
    __tablename__ = "properties"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    currency: Mapped[str] = mapped_column(String(10), nullable=False)  # Assuming currency is a short string like 'USD', 'EUR'
    city_lantin: Mapped[str] = mapped_column(String(100), nullable=False)
    city_cyrillic: Mapped[str] = mapped_column(String(100), nullable=False)
    area_lantin: Mapped[str] = mapped_column(String(100), nullable=False)
    area_cyrillic: Mapped[str] = mapped_column(String(100), nullable=False)
    type: Mapped[str] = mapped_column(String(50), nullable=False)  # Store as string to match choices
    size: Mapped[int] = mapped_column(Integer, nullable=False)
    bedrooms: Mapped[int] = mapped_column(Integer)  # Nullable since it's optional
    bathrooms: Mapped[int] = mapped_column(Integer)  # Nullable since it's optional
    description_en: Mapped[str] = mapped_column(Text)  # CKEditor content should be stored as text
    description_bg: Mapped[str] = mapped_column(Text, nullable=False)
    description_ru: Mapped[str] = mapped_column(Text)  # Optional field

