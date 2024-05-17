# Projeto Django - Tela Inicial

## Introdução
Este é um guia para  projeto Adote Um Pet. Ele inclui instruções sobre como configurar um ambiente virtual, instalar pacotes necessários e executar o projeto.

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

### 4. Remova o "-example do arquivo .env"

Para configurar corretamente o arquivo `.env`, remova o sufixo `-example` do nome do arquivo.

Cria sua api [aqui](https://console.cloud.google.com/project).
`https://console.cloud.google.com/project`
```env
client_id="COLOQUE AQUI SUA CLIENT-ID DO API DO GMAIL"
secret="COLOQUE AQUI A SECRECT-KEY DO GMAIL"
```

### 5. Execução do Projeto Django
Após instalar as dependências, você pode rodar o projeto Django:

```bash
python manage.py runserver
```

O servidor de desenvolvimento será iniciado e você poderá acessar o projeto em `http://localhost:8000/`.

## Conclusão
Agora você está pronto para começar a desenvolver seu projeto.
Certifique-se de manter seu ambiente virtual ativado sempre que estiver trabalhando no projeto.



# Padrões de Codificação

Neste projeto, adotamos uma abordagem  para manter a consistência e a legibilidade do código. Abaixo estão as ferramentas e configurações que utilizamos:

## Ferramentas de Formatação de Código

Utilizamos as seguintes ferramentas para garantir a padronização do código:

- **Black**: Ferramenta de formatação de código Python que garante que todo o código Python seja formatado de maneira consistente.
- **isort**: Utilizado para organizar automaticamente as importações em ordem alfabética e agrupadas logicamente.
- **Taskipy**: Uma ferramenta que nos permite configurar atalhos para execução de comandos comuns, facilitando o processo de padronização e manutenção do código.

Certifique-se de executar essas ferramentas regularmente para manter o código formatado corretamente.

## Configuração do `.editorconfig`

O arquivo `.editorconfig` na raiz do projeto define algumas configurações para garantir a consistência do estilo de codificação em diferentes editores. Aqui está o conteúdo desse arquivo:

 EditorConfig is awesome: `https://EditorConfig.org`

```ini
root = true

[*]
indent_style = space
indent_size = 4
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true
```

Essas configurações ajudam a manter uma base sólida para a formatação do código em diferentes ambientes de desenvolvimento.

## Configuração do Taskipy

Além das configurações padrão para Black e isort, também configuramos atalhos úteis usando o Taskipy. Aqui está um exemplo de configuração no arquivo `pyproject.toml`:

```toml
[tool.pytest.ini_options]
pythonpath = "."
addopts = "--doctest-modules"

[tool.isort]
profile = "black"
line_length = 79

[tool.taskipy.tasks]
check = "black --check --diff . && isort --check --diff ."
correct = "black . && isort ."
docs = "mkdocs serve"
test = "pytest -s -x -vv"
post_test = "coverage html"
```

Com esses atalhos configurados, podemos executar tarefas comuns de padronização e teste com facilidade, por exemplo:

- `task check`: Verifica se o código está formatado corretamente e as importações estão ordenadas.
- `task correct`: Formata o código e organiza as importações de acordo com as configurações definidas.
- `task docs`: Inicia o servidor de desenvolvimento do MkDocs para visualização da documentação.
- `task test`: Executa os testes com o Pytest, exibindo informações detalhadas.
- `task post_test`: Gera relatórios de cobertura após a execução dos testes.
