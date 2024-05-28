from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, Float, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType
from database import Base

class User(Base):
    __table_name__ = 'user'


    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=True)
    last_name = Column(String(20), nullable=True)
    username = Column(String(10), unique=True)
    email = Column(Text, nullable=True)
    password = Column(String(20), nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    order = relationship('orders', back_populates='user')

    def __repr__(self):
        return self.first_name

class Category(Base):

    __table_name__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    product = relationship('product', back_populates='category')




class Product(Base):

    __table_name__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    descriptions = Column(Text)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('category',back_populates='product')
    order = relationship('Order', back_populates='product')





class Order(Base):
    __table_name__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    user = relationship("user", back_populates='orders')
    product = relationship('Product', back_populates='orders' )





