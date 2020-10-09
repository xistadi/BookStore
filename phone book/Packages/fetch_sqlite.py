from sqlalchemy import create_engine
from sql_cr import Users, Phone_numbers, Base
from sqlalchemy.orm import sessionmaker

def fetch_sqlite():
    engine = create_engine('sqlite:///../db/sqlalchemy_phone_book.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()

    line = "=" * 80

    print(f"{line}\nID\tФИО\t\t\tАдрес\t\t\tНомер")
    query = session.query(Users, Phone_numbers)
    query = query.join(Users, Users.id == Phone_numbers.user_id)
    records = query.all()
    for user, phone in records:
        print(f"{user.id}\t{user.name}\t\t{user.address}\t\t{phone.phone_number}")
    print(line)

if __name__ == "__main__":
    fetch_sqlite()