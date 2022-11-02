import os

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = os.environ.get('USER'),
        senha = os.environ.get('PASSWORD'),
        servidor = 'localhost',
        database = 'game_list'
    )