from sqlalchemy import create_engine
from sql_cr import Users, Phone_numbers, Base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sqlalchemy_phone_book.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

line = "=" * 60

print(f"{line}\nФИО\t\t\tАдрес\t\t\tНомер")
query = session.query(Users, Phone_numbers)
query = query.join(Users, Users.id == Phone_numbers.user_id)
records = query.all()
for user, phone in records:
	print(f"{user.name}\t\t{user.address}\t\t{phone.phone_number}")
print(line)