import os
from main import app


def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        boolean = f'{id}.jpg' == nome_arquivo
        if boolean:
            return nome_arquivo



def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    if arquivo is None:
        return
    else:
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))
