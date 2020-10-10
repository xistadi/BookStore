from sqlalchemy import create_engine
from Packages.models import Users, Phone_numbers, Base
from sqlalchemy.orm import sessionmaker

def update_db():
    # обновить данные(имя и адрес) пользователя по id 
    engine = create_engine('sqlite:///sqlalchemy_phone_book.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()
    try:
        kekid = input("Id: ")
        newname = input("New name: ")
        newnaddress = input("New address: ")
        user = session.query(Users).filter_by(id=kekid).first()
        user.address = newnaddress
        user.name = newname
        session.commit()
        print(f"\nОбновлены данные для {user.name}!\n")
        input("Чтобы подолжить нажмите Enter")
    except: 
        print(f"\nПользователя под таким id не существует!\n")
        input("Чтобы подолжить нажмите Enter")

if __name__ == "__main__":
    update_db()