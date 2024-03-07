from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

#need to call load because we are using a .env file

load_dotenv()

#connect to database using env variable

#engine manages overall connection to the db
#Session generators temporary connections for CRUD
#Base class variable helps us map models to real mySQL tables

engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()
