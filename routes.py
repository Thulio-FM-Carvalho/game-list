from pydantic import ValidationError

from main import app, db
from flask import request
from models import GameForm
from service import Service

game_service = Service()


@app.route('/jogos', methods=['POST'])
def add_game():
    data = request.get_json()

    try:
        form = GameForm(**data)
        game_service.send_data(form)
    except ValidationError as e:
        return {
                   'title': 'Erro de validação',
                   'details': e.errors()
               }, 400
    except Exception as er:
        return {
                   'title': "Erro interno no servidor",
                   'content': "Por favor, tente novamente."
               }, 500
    return '', 201


@app.route('/jogo/<int:game_id>', methods=['DELETE'])
def remove_game(game_id):
    bool = game_service.del_data(game_id)

    if bool:
        return "", 204
    else:
        return "", 404


@app.route('/jogos', methods=['GET'])
def get_all_game():
    games = game_service.get_all_games()
    records = [z.to_json() for z in games]
    return records, 200


@app.route('/jogo/<int:game_id>', methods=['GET'])
def find_game_by_id(game_id):
    game = game_service.get_game_by_id(game_id)
    if game:
        return "", 404
    else:
        records = game.to_json()
    return records, 200


@app.route('/jogo/<int:game_id>', methods=['PUT'])
def update_game(game_id):
    data = request.get_json()
    name = data['name']
    category = data['category']
    console = data['console']
    game = game_service.update_game_by_id(game_id, name, category, console)

    if game:
        return "", 200
    else:
        return "", 404
