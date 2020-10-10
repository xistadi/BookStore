from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Packages.models import Users, Phone_numbers, Base

def insert_sql():
    # ввод нового пользователя
    engine = create_engine('sqlite:///sqlalchemy_phone_book.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    
    a, b, c =input("Введите ФИО: "), input("Adress: "), input("Mobile phone number: ")
    username = Users(name=a, address=b)
    session.add(username)
    session.commit()
    
    username_phone_number = Phone_numbers(phone_number=c, user=username)
    session.add(username_phone_number)
    session.commit()
    print(f"\nДобавлен пользователь {username.name}!\n")
    input("Чтобы подолжить нажмите Enter")

if __name__ == "__main__":
    insert_sql()