# Introdução
Este é um guia para  projeto Adote Um Pet. Ele inclui instruções sobre como configurar um ambiente virtual, instalar pacotes necessários e executar o projeto.

Documentação: https://adote-um-pet-web.github.io/Documentation/


## Recomendado:
`PYTHON >= 3.11`
`Django == 5`

## Como Executar
Para executar o projeto, siga as etapas abaixo:

### 1. Criação de Ambiente Virtual
Para isolar as dependências do projeto, é recomendável criar um ambiente virtual. Utilize o seguinte comando:

```bash
# No diretório do seu projeto
python -m venv venv
```

### 2. Ativação do Ambiente Virtual
#### Windows
```bash
venv\Scripts\activate
```

#### Linux
```bash
source venv/bin/activate
```

### 3. Instalação de Pacotes
Com o ambiente virtual ativado, instale os pacotes necessários usando o `pip`:

```bash
pip install -r requirements.txt
```

Certifique-se de ter um arquivo `requirements.txt` com as dependências do seu projeto.


### 4. Remova o "-example do arquivo .env"

Para configurar corretamente o arquivo `.env`, remova o sufixo `-example` do nome do arquivo.

Exemplo:

![Remova o "-example do arquivo .env"](docs/img/env-example.png)

Deixa assim:

![.env](docs/img/env.png)



### 5. Configuração do Banco de Dados
Este projeto carrega dados do banco de dados utilizando o gerenciador Python `makemigrations` e `migrate`.

Antes de começar, certifique-se de ter configurado corretamente o banco de dados. Para isso, execute os seguintes comandos:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Execução do Projeto
Após instalar as dependências, você pode rodar o projeto:

```bash
python manage.py runserver
```

O servidor de desenvolvimento será iniciado e você poderá acessar o projeto em `http://localhost:8000/`.


# Atalhos

### Executando a Documentação

Para visualizar a documentação, você pode utilizar o MkDocs. Execute o seguinte comando:

```bash
mkdocs serve
```

Você também pode usar o atalho `task docs` para iniciar o servidor da documentação.

### Executando os Testes

Para executar os testes, utilize o pytest. Basta rodar o seguinte comando:

```bash
pytest
```

Alternativamente, você pode utilizar o atalho `task test` para rodar os testes.

### Com esses atalhos configurados, podemos executar tarefas comuns de padronização e teste com facilidade, por exemplo:

- `task check`: Verifica se o código está formatado corretamente e as importações estão ordenadas.
- `task correct`: Formata o código e organiza as importações de acordo com as configurações definidas.
- `task docs`: Inicia o servidor de desenvolvimento do MkDocs para visualização da documentação.
- `task test`: Executa os testes com o Pytest, exibindo informações detalhadas.
- `task post_test`: Gera relatórios de cobertura após a execução dos testes.



# Configuração extra `.env`:

### API-Gmail
Api do gmail para poder habilitar login via google

Cria sua api [aqui](https://console.cloud.google.com/project).
`https://console.cloud.google.com/project`
```bash
client_id="COLOQUE AQUI SUA CLIENT-ID DO API DO GMAIL"
secret="COLOQUE AQUI A SECRECT-KEY DO GMAIL"
```

### Enviu-Email

Habilita Configuração para poder enviar email pro usuario

```bash
EMAIL_HOST = 'SEU PROVEDOR EMAIL'
EMAIL_POST = 'USA PORTA'
EMAIL_USE_TLS = True
EMAIL_HOST_USER ='SEU EMAIL APP'
EMAIL_HOST_PASSWORD ='SUA SENHA APP EMAIL'
```
### Usa-database-Postgres

Se deseja altera o banco de dados adicione essa configuração
#### Postgres

```bash
DATABASE_ENGINE='django.db.backends.postgresql'
DATABASE_NAME="NOME SUA DATABSE"
DATABASE_USER = "NOME DE USER"
DATABASE_PASSWORD = "SENHA DO DB"
DATABASE_HOST = "HOST-DB"
DATABASE_PORT = "PORT-DB"
```
