# Indrodução
Esse é um mini-projeto em que utilizo o *Selenium* para mandar um email usando uma conta outlook para um destinatario qualquer.

# Como usar?
Antes de rodar a aplicação, você deve criar um ambiente virtual.
```bash
$ python -m venv venv
$ source venv/Scripts/active
$ pip install -r requirements.txt
```

Para a segurança, adicione as informações necessárias para acessar seu email criando um .env seguindo o .env_example.
```bash
EMAIL = "seuemail@outlook.com"
PASSWORD = "suasenha@2003"
```

Agora para rodar digite no cmd:
```bash
$ python enviar_email.py
```
