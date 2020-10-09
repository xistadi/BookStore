from sqlalchemy import create_engine
from sql_cr import Users, Phone_numbers, Base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///../db/sqlalchemy_phone_book.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


kekid = input("Id: ")
newname = input("New name: ")
newnaddress = input("New address: ")
user = session.query(Users).filter_by(id=kekid).first()
user.address = newnaddress
user.name = newname
session.commit()
print(f"Обновлены данные для {user.name}!")