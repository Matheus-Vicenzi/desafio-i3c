# desafio-i3c

## Dependencias
- Python 3.10.12
- openpyxl
- mysql-connector
- FastApi
- Uvicorn
- MySql
- DotEnv
- Docker(Opcional)

## Como iniciar a aplicação
- python3.10.12 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- docker compose up -d (Caso esteja utilizando docker, para subir um container mysql)
- inserir as configurações de conexão do banco de dados e caminho para o arquivo excel no arquivo src/infra/.env
- executar o script init.sql no banco de dados
- cd src
- python main.py
