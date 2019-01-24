from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :

class Charity(Base):
	__tablename__= "charity"
	id = Column(Integer,primary_key = True)
	name = Column(String)
	description = Column(String)
	url = Column(String)
	pic1 = Column(String)
	pic2 = Column(String)
	pic3 = Column(String)





