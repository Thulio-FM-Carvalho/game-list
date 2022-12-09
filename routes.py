import base64
from codecs import encode
from pydantic import ValidationError

from helpers import recupera_imagem
from main import app
from flask import request, session
from models import GameForm
from service import Service

game_service = Service()


@app.route('/jogo', methods=['POST'])
def add():
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


@app.route('/jogo', methods=['GET'])
def get_all():
    games = game_service.get_all_games()
    records = [z.to_json() for z in games]
    return records, 200


@app.route('/jogo/<int:game_id>', methods=['GET'])
def get_by_id(game_id):
    game = game_service.get_game_by_id(game_id)
    if game:
        records = game.to_json()

        img = recupera_imagem(game_id)
        with open(f"uploads/{img}", "rb") as img_file:
            my_string = base64.b64encode(img_file.read())

        records['img'] = my_string.decode('utf-8')

    else:
        return "", 404
    return records, 200


@app.route('/jogo/<int:game_id>', methods=['PUT'])
def update(game_id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        print("Usuário não logado. Por favor faça o login para adicionar novos jogos.")
        return "", 401

    data = request.get_json()
    name = data['name']
    category = data['category']
    console = data['console']
    img = data['img']
    game = game_service.update_game_by_id(game_id, name, category, console, img)

    if game:
        return "", 200
    else:
        return "", 404


@app.route('/jogo/<int:game_id>', methods=['DELETE'])
def remove(game_id):
    bool = game_service.del_data(game_id)

    if bool:
        return "", 204
    else:
        return "", 404


@app.route('/login', methods=['POST'])
def auth():
    data = request.get_json()
    user_form = data['nome']
    password_form = data['senha']

    auth = game_service.auth(user_form, password_form)

    if auth:
        return "", 200
    else:
        return "", 404


@app.route('/logout', methods=['GET'])
def logout():
    session['usuario_logado'] = None
    return "", 200


@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    files = data['img_data']

    base64_img = files
    bytes_img = encode(base64_img, 'utf-8')
    binary_img = base64.decodebytes(bytes_img)

    with open("uploads/imageToSave.jpg", "wb") as fh:
        fh.write(binary_img)
    return "", 200
