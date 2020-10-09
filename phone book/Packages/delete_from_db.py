from sqlalchemy import create_engine
from sql_cr import Users, Phone_numbers, Base
from sqlalchemy.orm import sessionmaker

def delete_from_db():
    engine = create_engine('sqlite:///../db/sqlalchemy_phone_book.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()



    kekid = input("Id: ")
    user = session.query(Users).filter_by(id=kekid).first()
    session.delete(user)
    session.commit()
    print(f"Удалены данные для id {kekid}!")

if __name__ == "__main__":
    delete_from_db()