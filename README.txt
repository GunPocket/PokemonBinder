# Pokémon Binder

Pokémon Binder é um projeto simples desenvolvido para praticar habilidades em backend utilizando Flask e Python. Ele funciona como um binder digital para organizar e registrar cartas de Pokémon.
Funcionalidades

    - Registro de cartas com nome, tipo e número serial.
    - Organização por tipo: Pokémon, Treinador ou Energia.
    - Filtros e ordenação por:
        - Tipo de carta.
        - Nome (ordem alfabética).
        - Menor valor.
        - Maior valor.
    - Registro e exibição de preço mínimo, com tooltip indicando a última data de atualização.
    - Link direto para o site da Liga Pokémon ao clicar no nome da carta.

## Tecnologias Utilizadas

    - Python 3.9+
    - Flask
    - Flask-SQLAlchemy
    - Bootstrap 5

## Instalação

    1. Clone o repositório:

```git clone https://github.com/gunpocket/pokemonbinder.git
cd pokemon-binder```

    2. Crie um ambiente virtual e instale as dependências:

```python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt```

    3. Inicie o servidor Flask:

    ```flask run```

    4. Acesse o projeto no navegador: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Estrutura do Projeto

    - `app.py`: Lida com as rotas e a lógica principal da aplicação.
    - `models.py`: Define o modelo para o banco de dados utilizando SQLAlchemy.
    - `templates/`: Contém os arquivos HTML organizados para o Flask.
    - `static/style.css`: Arquivo de estilos customizados para a aplicação.
    - `pokemon_cards.db`: Banco de dados SQLite para armazenar as cartas.

## Melhorias Futuras

    - Adicionar autenticação para múltiplos usuários.
    - Implementar API para integração com outras ferramentas.
    - Melhorar a interface com mais interatividade.

### Licença

Este projeto é licenciado sob a Creative Commons Attribution 4.0 International. Você pode usar, modificar e distribuir este projeto, desde que mantenha a atribuição ao autor.