# AppPizzaria

Aplicativo que simula algumas funcionalidades que uma pizzaria deve ter: cadastro de pizzas, bebidas e doces, realização de pedidos e cadastro e login de usuários.

## Passo a passo para rodar a API
* Instalação do Python: https://www.python.org/downloads/

* Certifique-se de que o pip e o virtualenv estão instalados;

* Após a instalação, clone o repositório: https://github.com/LucasAndradeF/pizza-app ou baixe o projeto pelo GitHub.

* Crie um ambiente virtual na pasta "pizza-app" com o comando no terminal: `python -m venv venv`

* Ative o ambiente virtual (Windows): `venv\Scripts\activate`

* Instale as dependências necessárias para rodar a aplicação: `pip install -r requirements.txt`

* Execute a aplicação com o comando: `flask run --host=0.0.0.0`

* Altere a URL do código "index.js" para o IPv4 da sua máquina local, para que as requisições realizadas pelo emulador (Android Studio) funcionem corretamente.

## Requisitos para rodar o projeto no Android Studio

Para rodar o projeto no emulador do Android Studio, siga os passos abaixo:

1. **Instalar o Android Studio**:
   - Faça o download do Android Studio [aqui](https://developer.android.com/studio).
   - Siga as instruções para instalação conforme o seu sistema operacional.

2. **Criar um emulador no Android Studio**:
   - Siga as instruções para configurar o emulador de acordo com as especificações desejadas.

3. **Rodar o projeto no emulador**:
   - Após criar o emulador, inicie-o.
   - Vá para o diretório `AppPizzaria` e use o comando abaixo no terminal para rodar a aplicação no emulador:
     ```
     cordova run android
     ```

## Tecnologias utilizadas:
* Android Studio
* HTML5
* CSS3
* JavaScript
* Flask
* SQLite
* Python
* Framework Bulma
* SQLAlchemy
* Apache Cordova

## Telas do projeto

* Tela de Login

![Tela de Login](/AppPizzaria/www/img/telas/login.png)

* Tela de Cadastro

![Tela de Cadastro](/AppPizzaria/www/img/telas/cadastro.png)

* Menu

![Menu](/AppPizzaria/www/img/telas/menu.png)

* Cardápio

![Cardápio](/AppPizzaria/www/img/telas/cardapio-pizza.png)

* Pedidos

![Pedidos](/AppPizzaria/www/img/telas/pedidos-2.png)

* Informações

![Informações](/AppPizzaria/www/img/telas/info.png)

