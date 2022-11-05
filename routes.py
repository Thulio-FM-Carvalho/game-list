from pydantic import ValidationError

from main import app, db
from flask import request, session
from models import GameForm
from service import Service

game_service = Service()


@app.route('/jogos', methods=['POST'])
def add_game():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        print("Usuário não logado. Por favor faça o login para adicionar novos jogos.")
        return "", 401

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
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        print("Usuário não logado. Por favor faça o login para adicionar novos jogos.")
        return "", 401

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
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        print("Usuário não logado. Por favor faça o login para adicionar novos jogos.")
        return "", 401

    data = request.get_json()
    name = data['name']
    category = data['category']
    console = data['console']
    game = game_service.update_game_by_id(game_id, name, category, console)

    if game:
        return "", 200
    else:
        return "", 404


@app.route('/autenticar', methods=['POST'])
def autenticar():

    data = request.get_json()
    user_form = data['nome']
    password_form = data['senha']

    auth = game_service.autenticar(user_form, password_form)

    if auth:
        return "", 200
    else:
        return "", 404


@app.route('/logout', methods=['GET'])
def logout():
    session['usuario_logado'] = None
    return "", 200
