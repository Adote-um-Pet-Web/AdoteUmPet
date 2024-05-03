# Introdução
Este é um guia para  projeto Adote Um Pet. Ele inclui instruções sobre como configurar um ambiente virtual, instalar pacotes necessários e executar o projeto.

Documentação: https://adote-um-pet-web.github.io/Documentation/

## Recomendado:
`PYTHON >= 3.11`
`Django == 5.0.3`

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

### 4. Execução do Projeto Django
Após instalar as dependências, você pode rodar o projeto Django:

```bash
python manage.py runserver
```

O servidor de desenvolvimento será iniciado e você poderá acessar o projeto em `http://localhost:8000/`.

# Uso

Este projeto carrega dados do banco de dados utilizando o gerenciador Python `makemigrations` e `migrate`.

### Configuração do Banco de Dados

Antes de começar, certifique-se de ter configurado corretamente o banco de dados. Para isso, execute os seguintes comandos:

```bash
python manage.py makemigrations
python manage.py migrate
```

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
