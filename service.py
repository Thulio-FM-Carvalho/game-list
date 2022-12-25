import base64
from codecs import encode

from flask import session

from helpers import deleta_arquivo
from models import GameForm, Jogos, Usuarios
from main import db, app
from flask_bcrypt import check_password_hash


class Service:

    def send_data(self, form_data: GameForm):
        name = form_data.name
        category = form_data.category
        console = form_data.console
        base64_img = form_data.img

        game = Jogos.query.filter_by(nome=name).first()

        if game:
            print("Jogo já existente. Por favor tente adicionar outro jogo.")
            raise
        else:
            new_game = Jogos(nome=name, categoria=category, console=console)
            db.session.add(new_game)
            db.session.commit()

        bytes_img = encode(base64_img, 'utf-8')
        binary_img = base64.decodebytes(bytes_img)

        upload_path = app.config['UPLOAD_PATH']

        with open(f'{upload_path}/{new_game.id}.jpg', "wb") as fh:
            fh.write(binary_img)

    def get_all_games(self):

        games = Jogos.query.all()

        return games

    def get_game_by_id(self, game_id):
        game = Jogos.query.filter_by(id=game_id).first()
        if game == None:
            print("Não existe nenhum jogo com esse ID no banco de dados")

        else:
            return game

    def update_game_by_id(self, game_id, name, category, console, img):
        game = Jogos.query.filter_by(nome=name).first()
        if game:
            print("Jogo já existente.")
        else:
            game = Jogos.query.filter_by(id=game_id).update(dict(nome=name, categoria=category, console=console))

            upload_path = app.config['UPLOAD_PATH']
            deleta_arquivo(game_id)

            bytes_img = encode(img, 'utf-8')
            binary_img = base64.decodebytes(bytes_img)

            with open(f'{upload_path}/{game_id}.jpg', "wb") as fh:
                fh.write(binary_img)

            if game == 0:
                print("Não existe nenhum jogo com este ID no banco de dados.")
                return False
            else:
                db.session.commit()
                return True

    def del_data(self, game_id):

        result = Jogos.query.filter_by(id=game_id).delete()
        if result == 0:
            print("Não existe nenhum jogo com este ID no banco de dados.")
            return False
        else:
            deleta_arquivo(game_id)
            db.session.commit()
            return True

    def auth(self, user_form, password_form):
        usuario = Usuarios.query.filter_by(nome=user_form).first()

        senha = check_password_hash(usuario.senha, password_form)

        if usuario and senha:
            print("Usuário logado com sucesso.")
            session['usuario_logado'] = usuario.nome
            return True
        else:
            print("Usuario não logado, por favor tente novamente.")
            return False
