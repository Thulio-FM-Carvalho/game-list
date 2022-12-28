# game-list

* [Índice](#índice)
* [Descrição do Projeto](#descrição-do-projeto)
* [Funcionalidades](#funcionalidades)
* [Aplicação](#aplicação)
* [Ferramentas utilizadas](#ferramentas-utilizadas)
* [Frameworks e tecnologias utilizadas](#frameworks-e-tecnologias-utilizadas)
* [Pessoas Desenvolvedoras do Projeto](#pessoas-desenvolvedoras)

# Descrição do projeto
Game-list é uma API feita em Python que se dispõe ser consumida por uma aplicação Front-end. Das suas funcionalidades, é permitido cadastrar, listar, editar, remover jogos e fazer login e logout de um usuário. 
Com um sistema de autorização implementado, só será permitido cadastrar, editar e remover um jogo se o usuário estiver logado. A cada jogo cadastrado será salvo no banco de dados. As listagens de jogos, edição e remoção que são realizadas são execuções a partir de queries executadas em SQL.

# Funcionalidades
 - ✔️ `Funcionalidade 1`: Realizar login e logout com lógica de autorização
 - ✔️ `Funcionalidade 2`: Adicionar um jogo contendo o nome, categoria, console e opção de fazer upload da imagem do jogo
 - ✔️ `Funcionalidade 3`: Listar todos os jogos
 - ✔️ `Funcionalidade 4`: Editar um jogo
 - ✔️ `Funcionalidade 5`: Remover um jogo

# Aplicação

![GIF 20-12-2022 21-40-27](https://user-images.githubusercontent.com/48070981/208794686-bd464ce0-94d6-4af6-b05e-370a96caeed2.gif)

# Ferramentas utilizadas
- `PyCharm`
- `MySQL Workbench`
- `Postman`

# Frameworks e tecnologias utilizadas
- `Flask`
- `SQLAlchemy`
- `Paradigma de Orientação a objetos`
- `Python`
- `HTML`
- `SQL`

# Abrir e rodar a aplicação 
Após baixar o projeto, você pode abrir com o PyCharm. Para isso, na tela de launcher clique em:

- Open;
- Procure o local onde o projeto está e o selecione (Caso o projeto seja baixado via zip, é necessário extraí-lo antes de procurá-lo);
- Por fim clique em OK;

Se necessário, configurar o Python interpreter e fazer a instalação das bibliotecas incluídas no arquivo ```requirements.txt```. Abra o arquivo ```prepara_banco.py```, coloque o usuario e a senha da conexão do banco de dados, salve o arquivo e o execute. Após a execução, agora foi criado um banco de dados para armazenar os jogos que serão cadastrados e obter os dados de login de usuário. Feito isso, execute a o arquivo ```jogoteca.py``` e será mostrado no console da aplicação um link. 🏆 

### Tá, a aplicação já está em execução, mas como consumir a API?
Você pode consumir a API utilizando o Postman, sistes de testes de API ou utilizando uma aplicação Front-end em React Native por exemplo. Neste exemplo abaixo irei
utilizar o Postman para o consumo.

<details>
  <summary>Realizar login</summary>
  <ol>
    <li>Abra o Postman, clique no <code>+</code> para criar uma nova request, selecione o método <code>POST</code>, digite <code>localhost:5000/login</code>, coloque
    no corpo da requisição 1 objeto JSON contento os atributos <code>nome</code> e <code>senha</code> e seus respectivos valores e clique em <code>send</code>.</li>
    <p>Exemplo:</p>
    <p><img src="https://user-images.githubusercontent.com/48070981/209688367-115b4426-9a5a-4fed-94f6-7c634bb8b849.gif" alt="Login"></p>
    <p>Explicando o GIF acima, ao disparar a requisição a aplicação processou os valores dos atributos <code>login</code> e <code>senha</code>, verificou se existem 
    o usuario no banco de dados e se a senha está correta e fez o login. Somente usuario logado pode adicionar, editar e remover jogos. Se o usuário não estiver logado, 
    poderá apenas listar todos os jogos listar um jogo específico. No entanto, fazer o login é ideal para uma boa experiência.</p>
  <ol>
</details>
<details>
  <summary>Adicionar um jogo</summary>
  <ol>
    <li>Abra o Postman, clique no <code>+</code> para criar uma nova request, selecione o método <code>POST</code>, digite <code>localhost:5000/jogo</code>, 
    coloque no corpo da requisição 1 objeto JSON contendo os atributos <code>nome</code>, <code>categoria</code>, <code>console</code>, <code>img</code> contendo seus 
    respectivos valores, e clique em <code>send</code>.</li>
    <p>Exemplo</p>
    <p><img src="https://user-images.githubusercontent.com/48070981/209565756-c597d481-9e16-4e64-bbe4-481a00a28013.gif" alt="Adicionar jogo"></p>
    <p>Explicando o GIF acima, ao disparar a requisição, os valores dos atributos <code>nome</code>, <code>categoria</code> e <code>console</code> foram salvos no 
    banco de dados e o valor do atributo <code>img</code> foi convertido e salvo na pasta do sevidor. O valor do atributo <code>img</code> é um base64 de uma imagem 
    com o formato .jpeg, no entanto somente base64 de imagens com o formato .jpeg serão processados corretamente pela aplicação e salvos na pasta do servidor.</p>
  <ol>
</details>
<details>
  <summary>Listar todos jogos</summary>
  <ol>
    <li>Abra o Postman, clique no <code>+</code> para criar uma nova request, selecione o método <code>GET</code>, digite <code>localhost:5000/jogo </code> e clique 
    em <code>send</code>.</li>
    <p>Exemplo:</p>
    <p><img src="https://user-images.githubusercontent.com/48070981/209486925-aaff98de-6e88-4ec3-82d2-9d89393a97f2.gif" alt="GIF 25-12-2022 21-54-38"></p>
    <p>Como foi mostrado no GIF acima, ao disparar a requisição foi retornado todos os jogos que já estavam cadastrados.</p>
  <ol>
</details>
<details>
  <summary>Editar um jogo</summary>
  <ol>
    <li>Abra o Postman, clique no <code>+</code> para criar uma nova request, selecione o método <code>PUT</code>, digite <code>localhost:5000/jogo/{ID}</code>, 
    coloque no corpo da requisição 1 objeto JSON contendo o <code>nome</code> e seu valor, <code>categoria</code> e seu valor, <code>console</code> e seu valor, 
    <code>img</code> e seu valor, e clique em <code>send</code>.</li>
    <p>Exemplo:</p>
    <p><img src="https://user-images.githubusercontent.com/48070981/209735770-a384922e-9085-47d0-8852-a97424f32dd7.gif" alt="Editar"></p>
    <p>Como foi mostrado no GIF acima, foi necessário inserir o ID do jogo logo após o localhost:5000/jogo para fazer a edição do jogo em específico. No entanto, para
    que edição ocorra, é indispensável deixar de colocar o ID. Ao disparar a requisição, o jogo de ID número 30 será atualizado no banco de dados com os valores do 
    campo nome, categoria e console e a imagem novamente é convertida e salva na pasta do servidor.</p>
  </ol>
</details>
<details>
  <summary>Remover um jogo</summary>
   <ol>
    <li>Abra o Postman, clique no <code>+</code> para criar uma nova request, selecione o método <code>DEL</code>, digite <code>localhost:5000/jogo/{ID}</code> e 
    clique em <code>send</code>. Exemplo: </li>
    <p><img src="https://user-images.githubusercontent.com/48070981/209737931-87b65843-1ebb-4b92-80ee-1fb97b890aac.gif" alt="Remover"></p>
    <p>Como foi mostrado no GIF acima, foi necessário inserir o ID do jogo logo após o localhost:5000/jogo para fazer a remoção do jogo em específico. No entanto, para
    que a remoção ocorra, é indispensável deixar de colocar o ID. Ao disparar a requisição, o jogo de ID número 30 será removido do banco de dados e a imagem também é
    removida da pasta do servidor.</p>
  <ol>
</details>


# Autores

| [<img src="https://avatars.githubusercontent.com/u/48070981?s=400&v=4" width=115><br><sub>Thulio Carvalho</sub>](https://github.com/Thulio-FM-Carvalho) |  
| :---: |
