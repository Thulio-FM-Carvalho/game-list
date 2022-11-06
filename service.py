import base64
from codecs import encode

from flask import session

from models import GameForm, Jogos, Usuarios
from main import db


class Service:

    def send_data(self, form_data: GameForm):
        name = form_data.name
        category = form_data.category
        console = form_data.console
        imgd = form_data.img

        game = Jogos.query.filter_by(nome=name).first()

        if game:
            print("Jogo já existente. Por favor tente adicionar outro jogo.")
            raise
        else:
            new_game = Jogos(nome=name, categoria=category, console=console, img=imgd)
            db.session.add(new_game)
            db.session.commit()

    def del_data(self, game_id):

        result = Jogos.query.filter_by(id=game_id).delete()
        if result == 0:
            print("Não existe nenhum jogo com este ID no banco de dados.")
            return False
        else:
            db.session.commit()
            return True

    def get_all_games(self):

        games = Jogos.query.all()

        return games

    def get_game_by_id(self, game_id):
        game = Jogos.query.filter_by(id=game_id).first()
        if game == None:
            print("Não existe nenhum jogo com esse ID no banco de dados")

        else:
            return game

    def update_game_by_id(self, game_id, name, category, console):
        game = Jogos.query.filter_by(id=game_id).update(dict(nome=name, categoria=category, console=console))
        if game == 0:
            print("Não existe nenhum jogo com este ID no banco de dados.")
            return False
        else:
            db.session.commit()
            return True

    def autenticar(self, user_form, password_form):
        usuario = Usuarios.query.filter_by(nome=user_form).first()

        if usuario:
            if password_form == usuario.senha:
                print("Usuário logado com sucesso.")
                session['usuario_logado'] = usuario.nome
                return True
            else:
                print("Usuario não logado, por favor tente novamente.")
                return False
