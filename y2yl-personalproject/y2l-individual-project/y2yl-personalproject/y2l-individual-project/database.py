from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///charity.db?check_same_thread=False')


Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def get_all_charities():
    charities = session.query(Charity).all()
    return charities

def get_one_charity(id):
	charity = session.query(Charity).filter_by(id = id ).first()
	return charity

def add_charity(name,short_description,url,pic1,pic2,pic3):
	new_charity = Charity(name = name, description = short_description, url = url, pic1 = pic1, pic2 = pic2, pic3 = pic3)
	session.add(new_charity)
	session.commit()

def delete_charity(id):
	session.query(id).delete()
# delete_charity(get_all_charities())
# print(get_all_charities())

# add_charity("testing","we are hoping this will work",
#  "https://www.w3schools.com/bootstrap/bootstrap_theme_band.asp",
#  "https://i.ytimg.com/vi/SfLV8hD7zX4/maxresdefault.jpg"
#  , "https://i.ytimg.com/vi/SfLV8hD7zX4/maxresdefault.jpg"
# ,"https://i.ytimg.com/vi/SfLV8hD7zX4/maxresdefault.jpg")