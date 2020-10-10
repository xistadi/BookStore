from sqlalchemy import create_engine
from Packages.models import Users, Phone_numbers, Base
from sqlalchemy.orm import sessionmaker
from Packages.clear_screen import clear_screen

def fetch_sqlite():
    # вывод всех пользователей
    engine = create_engine('sqlite:///sqlalchemy_phone_book.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()
    clear_screen()
    line = "=" * 80

    print(f"{line}\nID\tФИО\t\t\tАдрес\t\t\tНомер")
    query = session.query(Users, Phone_numbers)
    query = query.join(Users, Users.id == Phone_numbers.user_id).order_by(Users.name)
    records = query.all()
    for user, phone in records:
        print(f"{user.id}\t{user.name}\t\t{user.address}\t\t{phone.phone_number}")
    print(line)
    input("Чтобы подолжить нажмите Enter")

if __name__ == "__main__":
    fetch_sqlite()