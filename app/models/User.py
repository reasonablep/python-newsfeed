from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
import bcrypt

#generate salt to hash passwords against

salt = bcrypt.gensalt()

#User class inherits from Base class 
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password= Column(String(100), nullable=False)

    @validates('email')
    def validate_email(self, key, email):

    # make sure the email contains @ chracter
        
        assert '@' in email
        return email
    
    @validates('password')
    def validate_password(self, key, password):
        assert len(password) > 4
        return bcrypt.hashpw(password.encode('utf-8'), salt) 