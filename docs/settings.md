# Configurações do Django para o projeto setup.

Gerado pelo 'django-admin startproject' usando Django 5.0.3.

Para mais informações sobre este arquivo, consulte [a documentação oficial](https://docs.djangoproject.com/en/5.0/topics/settings/).

Para a lista completa de configurações e seus valores, consulte [a documentação oficial](https://docs.djangoproject.com/en/5.0/ref/settings/).

## Django Configuração Social-Account
Este trecho de código Python configura as informações de autenticação OAuth para a integração de login social com a conta do Google em uma aplicação Django. Ele é usado para definir as credenciais do cliente necessárias para autenticar e autorizar usuários por meio do Google.
[https://docs.allauth.org/en/latest/](https://docs.allauth.org/en/latest/)

```python
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        # Para cada provedor baseado em OAuth, adicione um objeto ``SocialApp``
        # (aplicativo ``socialaccount``) contendo as credenciais de cliente necessárias,
        # ou liste-as aqui:
        "APP": {
            "client_id": os.getenv("client_id"),
            "secret": os.getenv("secret"),
            "key": "",
        }
    }
}
```
