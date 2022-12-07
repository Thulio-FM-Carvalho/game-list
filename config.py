import os

SECRET_KEY = 'alura'
#fazendo a conexão com o banco de dados
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'root',
        servidor = 'localhost',
        database = 'game_list'
    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'