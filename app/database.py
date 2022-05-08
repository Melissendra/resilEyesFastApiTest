from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# our database url
SQLALCHEMY_DATABASE_URL = 'sqlite:///./users.db'

# we define our engine to connect the application to our database 
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# Define our session: from the connection to the disconnection
SessionLocal = sessionmaker(bind=engine)

# Our model base for creating tables
Base = declarative_base()
