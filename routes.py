from pydantic import ValidationError

from main import app, db
from flask import request
from models import GameForm
from service import Service

game_service = Service()


@app.route('/add', methods=['POST'])
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
    return '', 200


@app.route('/remove/<int:game_id>', methods=['DELETE'])
def remove_game(game_id):
    id = game_id
    game_service.del_data(id)

    return "", 204

@app.route('/gamelist', methods=['GET'])
def get_all_game():
    return "", 200