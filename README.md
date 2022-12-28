# game-list

# Índice
* [Índice](#índice)
* [Descrição do Projeto](#descrição-do-projeto)
* [Funcionalidades](#funcionalidades)
* [Ferramentas utilizadas](#ferramentas-utilizadas)
* [Frameworks e tecnologias utilizadas](#frameworks-e-tecnologias-utilizadas)
* [Desenvolvedores do Projeto](#desenvolvedores)

# Descrição do projeto
Game-list é uma API feita em Python que se dispõe ser consumida por uma aplicação Front-end. Das suas funcionalidades, é permitido adicionar, listar, editar, remover jogos e fazer login e logout de um usuário. 
Com um sistema de autorização implementado, só será permitido adicionar, editar e remover um jogo se o usuário estiver logado. Cada jogo adicionado é guardado no banco de dados e cada a adição, listagem, edição e remoção de jogos é executada por instruções SQL.

# Funcionalidades
 - ✔️ `Funcionalidade 1`: Realizar login e logout com lógica de autorização
 - ✔️ `Funcionalidade 2`: Adicionar um jogo contendo o nome, categoria, console e opção de fazer upload da imagem do jogo
 - ✔️ `Funcionalidade 3`: Listar todos os jogos
 - ✔️ `Funcionalidade 4`: Editar um jogo
 - ✔️ `Funcionalidade 5`: Remover um jogo

# Ferramentas utilizadas
- `PyCharm`
- `MySQL Workbench`
- `Postman`

# Frameworks e tecnologias utilizadas
- `Flask`
- `SQLAlchemy`
- `Paradigma de Orientação a objetos`
- `Python`
- `SQL`

# Abrir e rodar a aplicação 
Após baixar o projeto, você pode abrir com o PyCharm. Para isso, na tela de launcher clique em:

- Open;
- Procure o local onde o projeto está e o selecione (Caso o projeto seja baixado via zip, é necessário extraí-lo antes de procurá-lo);
- Por fim clique em OK;

Se necessário, configurar o Python interpreter e fazer a instalação das bibliotecas incluídas no arquivo ```requirements.txt```. Abra o arquivo ```prepara_banco.py```, coloque o usuario e a senha da conexão do banco de dados, salve o arquivo e o execute. Após a execução, agora foi criado um banco de dados para armazenar os jogos que serão cadastrados e obter os dados de login de usuário. Feito isso, execute a o arquivo ```jogoteca.py``` para a inicalização da aplicação. 🏆 

### A aplicação já está em execução, mas como consumir a API?
Você pode consumir a API utilizando o Postman, sites de testes de API ou utilizando uma aplicação Front-end em React Native por exemplo. Neste exemplo abaixo irei
utilizar o Postman para o consumo.

<details>
  <summary>Realizar login</summary>
  <ol>
    <li>Abra o Postman, clique no <code>+</code> para criar uma nova request, selecione o método <code>POST</code>, digite <code>localhost:5000/login</code>, coloque
    no corpo da requisição 1 objeto JSON contento os atributos <code>nome</code> e <code>senha</code> e seus respectivos valores e clique em <code>send</code>.</li>
    <p>Exemplo:</p>
    <p><img src="https://user-images.githubusercontent.com/48070981/209688367-115b4426-9a5a-4fed-94f6-7c634bb8b849.gif" alt="Login"></p>
    <p>Explicando o GIF acima, ao disparar a requisição a aplicação processou os valores dos atributos <code>login</code> e <code>senha</code>, verificou se existe
    o usuario no banco de dados, se a senha está correta e fez o login. Somente usuario logado pode adicionar, editar e remover jogos. Se o usuário não estiver    
    logado, poderá apenas listar todos os jogos listar um jogo específico. No entanto, fazer o login é ideal para uma boa experiência.</p>
  <ol>
</details>
<details>
  <summary>Adicionar um jogo</summary>
  <ol>
    <li>Abra o Postman, clique no <code>+</code> para criar uma nova request, selecione o método <code>POST</code>, digite <code>localhost:5000/jogo</code>, 
    coloque no corpo da requisição 1 objeto JSON contendo os atributos <code>nome</code>, <code>categoria</code>, <code>console</code>, <code>img</code> contendo seus 
    respectivos valores, e clique em <code>send</code>.</li>
    <p>Exemplo:</p>
    <p><img src="https://user-images.githubusercontent.com/48070981/209565756-c597d481-9e16-4e64-bbe4-481a00a28013.gif" alt="Adicionar jogo"></p>
    <p>Explicando o GIF acima, ao disparar a requisição, os valores dos atributos <code>nome</code>, <code>categoria</code> e <code>console</code> foram salvos no 
    banco de dados e o valor do atributo <code>img</code> foi convertido e salvo na pasta do sevidor. O valor do atributo <code>img</code> é um base64 de uma imagem 
    com o formato .jpeg, no entanto somente base64 de imagens com o formato .jpeg serão processados corretamente pela aplicação e salvos na pasta do servidor.
    Para saber se o jogo foi adicionado, dispare uma requisição na rota de listar todos os jogos ou listar um jogo e verifique, ou acesse o banco de dados e consulte 
    os registros da tabela <code>jogos</code>.</p>
  <ol>
</details>
<details>
  <summary>Listar todos jogos</summary>
  <ol>
    <li>Abra o Postman, clique no <code>+</code> para criar uma nova request, selecione o método <code>GET</code>, digite <code>localhost:5000/jogo </code> e clique 
    em <code>send</code>.</li>
    <p>Exemplo:</p>
    <p><img src="https://user-images.githubusercontent.com/48070981/209486925-aaff98de-6e88-4ec3-82d2-9d89393a97f2.gif" alt="GIF 25-12-2022 21-54-38"></p>
    <p>Explicando o GIF acima, ao disparar a requisição foi retornado um array com vários objetos(jogos) que já foram incluídos anteriormente.</p>
  <ol>
</details>
<details>
  <summary>Editar um jogo</summary>
  <ol>
    <li>Abra o Postman, clique no <code>+</code> para criar uma nova request, selecione o método <code>PUT</code>, digite <code>localhost:5000/jogo/{ID}</code>, 
    coloque no corpo da requisição 1 objeto JSON contendo os atributos<code>nome</code>, <code>categoria</code>, <code>console</code>, <code>img</code> e seus     
    respectivos valores que quer editar, e clique em <code>send</code>.</li>
    <p>Exemplo:</p>
    <p><img src="https://user-images.githubusercontent.com/48070981/209735770-a384922e-9085-47d0-8852-a97424f32dd7.gif" alt="Editar"></p>
    <p>Como foi mostrado no GIF acima, foi necessário inserir o ID do jogo logo após o <code>localhost:5000/jogo/</code> para fazer a edição do jogo em específico. 
     No entanto, para que edição ocorra, é indispensável deixar de colocar o ID. Ao disparar a requisição, o jogo de ID número 30 será atualizado no banco de dados 
     com os valores dos atributos nome, categoria e console e a imagem novamente é convertida e salvo na pasta do servidor. Para saber se o jogo foi editado,   
     dispare uma requisição na rota de listar todos os jogos ou listar um jogo e verifique, ou acesse o banco de dados e consulte os registros da tabela              
     <code>jogos</code>.</p>
  </ol>
</details>
<details>
  <summary>Remover um jogo</summary>
   <ol>
    <li>Abra o Postman, clique no <code>+</code> para criar uma nova request, selecione o método <code>DEL</code>, digite <code>localhost:5000/jogo/{ID}</code> e 
    clique em <code>send</code>.</li>
    <p>Exemplo:</p>
    <p><img src="https://user-images.githubusercontent.com/48070981/209737931-87b65843-1ebb-4b92-80ee-1fb97b890aac.gif" alt="Remover"></p>
    <p>Como foi mostrado no GIF acima, foi necessário inserir o ID do jogo logo após o <code>localhost:5000/jogo/</code> para fazer a remoção do jogo em específico. 
    No entanto, para que a remoção ocorra, é indispensável deixar de colocar o ID. Ao disparar a requisição, o jogo de ID número 30 será removido do banco de dados 
    e a imagem também é removida da pasta do servidor. Para saber se o jogo foi adicionado, dispare uma requisição na rota de listar todos os jogos ou listar um jogo 
    e verifique, ou acesse o banco de dados e consulte os registros da tabela <code>jogos</code>.</p>
  <ol>
</details>


# Desenvolvedores

| [<img src="https://avatars.githubusercontent.com/u/48070981?s=400&v=4" width=115><br><sub>Thulio Carvalho</sub>](https://github.com/Thulio-FM-Carvalho) |  
| :---: |
