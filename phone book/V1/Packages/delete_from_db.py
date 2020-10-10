from sqlalchemy import create_engine
from Packages.models import Users, Phone_numbers, Base
from sqlalchemy.orm import sessionmaker

def delete_from_db():
    # удалить пользователя по id
    engine = create_engine('sqlite:///sqlalchemy_phone_book.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()
    try:
        kekid = input("Id: ")
        user = session.query(Users).filter_by(id=kekid).first()
        session.delete(user)
        session.commit()
        print(f"\nУдалены данные для id {kekid}!\n")
        input("Чтобы подолжить нажмите Enter")
    except: 
        print(f"\nПользователя под таким id не существует!\n")
        input("Чтобы подолжить нажмите Enter")

if __name__ == "__main__":
    delete_from_db()