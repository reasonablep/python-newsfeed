from app.db import Base
from sqlalchemy import Column, Integer, ForeignKey

class Vote (Base):
    __tablename__= 'votes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))

    # This model does not store any unique information
    # Posts model will count the votes using a reference to this model
