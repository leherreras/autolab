from app import db
from models.user import User
from utils.import_db import load_data


def install():
    db.create_all()
    load_data()

    user = User(
        name="Test",
        api_key="123456"
    )
    db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    install()
