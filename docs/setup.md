# Configurações do Django para o projeto setup.

Gerado pelo 'django-admin startproject' usando Django 5.0.3.

Para mais informações sobre este arquivo, consulte [a documentação oficial](https://docs.djangoproject.com/en/5.0/topics/settings/).

Para a lista completa de configurações e seus valores, consulte [a documentação oficial](https://docs.djangoproject.com/en/5.0/ref/settings/).

```python

from pathlib import Path
import os

# Construa caminhos dentro do projeto assim: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "djangaedsdo-insecure-6n@haxmlndsdsdsdsd&u*gs*y2sbodhna43sbesdsddsdsdsd++v3ex6lvcpp3ga_bkmk"


DEBUG = True

ALLOWED_HOSTS = []

# Definição de aplicativos

INSTALLED_APPS = [
    "jazzmin",  # Tema Django-admin
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Meus aplicativos
    "userprofile",
    "pet",
    "adoption",
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",  # Adiciona headers de segurança
    "django.contrib.sessions.middleware.SessionMiddleware",  # Gerenciamento de sessão
    "django.middleware.common.CommonMiddleware",  # Funcionalidades comuns
    "django.middleware.csrf.CsrfViewMiddleware",  # Proteção contra CSRF
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # Autenticação de usuário
    "django.contrib.messages.middleware.MessageMiddleware",  # Mensagens
    "django.middleware.clickjacking.XFrameOptionsMiddleware",  # Proteção contra clickjacking
]

# Configuração de URL
ROOT_URLCONF = "setup.urls"

# Configuração de Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",  # Backend do template
        "DIRS": [
            BASE_DIR / "templates",  # Diretórios de templates
        ],
        "APP_DIRS": True,  # Habilita a procura por templates nos diretórios dos aplicativos
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI Application
WSGI_APPLICATION = "setup.wsgi.application"

# Banco de dados
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # Backend do banco de dados
        "NAME": BASE_DIR / "db.sqlite3",  # Nome do banco de dados
    }
}

# Validação de senha
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # Verifica similaridade com atributos do usuário
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # Verifica o comprimento mínimo da senha
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # Verifica senhas comuns
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # Verifica senhas numéricas
    },
]

# Internacionalização
LANGUAGE_CODE = "en-us"  # Código do idioma padrão
TIME_ZONE = "UTC"  # Fuso horário padrão
USE_I18N = True  # Ativa a internacionalização
USE_TZ = True  # Ativa o suporte para fuso horário

# Arquivos estáticos
STATIC_URL = "/static/"  # URL para arquivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, "static")  # Diretório para coletar arquivos estáticos
STATICFILES_DIRS = [os.path.join(BASE_DIR, "templates/static")]  # Diretórios adicionais para arquivos estáticos
MEDIA_URL = "/media/"  # URL para arquivos de mídia
MEDIA_ROOT = os.path.join(BASE_DIR, "media")  # Diretório para arquivos de mídia

# Tipo de campo de chave primária padrão
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"  # Define o tipo de campo padrão para chaves primárias


```
