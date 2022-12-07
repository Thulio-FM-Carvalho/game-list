from pydantic import BaseModel
from main import db


class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "categoria": self.categoria,
            "console": self.console,
        }


class Usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class GameForm(BaseModel):
    id: str = None
    name: str
    category: str
    console: str
    img: str = None
