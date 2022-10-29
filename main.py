from flask import Flask, request
from pydantic import BaseModel, ValidationError

app = Flask(__name__)

class GameForm(BaseModel):
    name: str = None
    category: str = None
    console: str = None

def send_data(form_data: GameForm):
    return print(form_data)

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
    return data, 200

if __name__ == '__main__':
    app.run(debug=True)
