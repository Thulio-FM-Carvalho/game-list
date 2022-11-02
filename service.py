from models import GameForm, Jogos
from main import db


class Service:

    def send_data(self, form_data: GameForm):
        name = form_data.name
        category = form_data.category
        console = form_data.console

        game = Jogos.query.filter_by(nome=name).first()

        if game:
            print("Jogo já existente. Por favor tente adicionar outro jogo.")
            raise
        else:
            new_game = Jogos(nome=name, categoria=category, console=console)
            db.session.add(new_game)
            db.session.commit()

    def del_data(self, game_id):

        game_id = Jogos.query.filter_by(id=game_id).first()
        if not game_id:
            print("Não existe nenhum jogo com este ID no banco de dados.")
        else:
            Jogos.query.filter_by(id=game_id).delete()
            db.session.commit()
