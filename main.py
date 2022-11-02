from flask import Flask, request
from pydantic import BaseModel, ValidationError

app = Flask(__name__)


class GameForm(BaseModel):
    name: str = None
    category: str = None
    console: str = None


def send_data(form_data: GameForm):
    name = form_data.name
    category = form_data.category
    console = form_data.console

    form = GameForm(name=name, category=category, console=console)
    lista = []
    lista.append(form)

    for game in lista:
        print(game.name, game.category, game.console)


def del_data(game_id: int, form_data: GameForm):
    return print(game_id)


@app.route('/gamelist', methods=['GET'])
def get_all_game():
    return "", 200


@app.route('/add', methods=['POST'])
def add_game():
    data = request.get_json()

    try:
        form = GameForm(**data)
        send_data(form)
    except ValidationError as e:
        return {
            'title': 'Erro de validação',
            'details': e.errors()
        }
    return '', 200


@app.route('/remove/<game_id>', methods=['DELETE'])
def remove_game(game_id: int):
    id = request.get_json()

    try:
        form = GameForm(**id)
        del_data(form, game_id)
    except ValidationError as e:
        return {
            'title': 'Erro de validação',
            'details': e.errors()
        }
    return id, 200


if __name__ == '__main__':
    app.run(debug=True)
