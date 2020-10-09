from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from sql_cr import Users, Phone_numbers, Base
 

engine = create_engine('sqlite:///../db/sqlalchemy_phone_book.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

kekid = input("ID: ")
c = input("Number: ")
username = session.query(Users).filter_by(id=kekid).first()
username_phone_number = Phone_numbers(phone_number=c, user=username)
session.add(username_phone_number)
session.commit()

print(f"Обновлен новый номер телефона для ID {kekid}!")