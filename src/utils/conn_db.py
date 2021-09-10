from flask_sqlalchemy import SQLAlchemy


def conn(app):
    """
    Create the connection to DB
    :param app: the app building by Flask
    :return: the db connection
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///autolab.db'
    db = SQLAlchemy(app)
    return db
