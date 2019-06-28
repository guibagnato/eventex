# Welcome to the Django

[![Build Status](https://travis-ci.org/guibagnato/eventex.svg?branch=master)](https://travis-ci.org/guibagnato/eventex)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/77ea81cc53cb46ef99d678e810675605)](https://app.codacy.com/app/guibagnato/eventex?utm_source=github.com&utm_medium=referral&utm_content=guibagnato/eventex&utm_campaign=Badge_Grade_Dashboard)

## Como desenvolver

 1. Clone o repositório
 2. Crie um virtualenv com Python 3.5
 3. Ative o virtualenv.
 4. Instale as dependências.
 5. Configure a instância com o .env
 6. Execute os testes.

```console
git clone git@github.com:guibagnato/eventex.git xttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy

 1. Crie uma instância no heroku
 2. Envie as configurações para o heroku
 3. Defina uma SECRET_KEY segura
 4. Defina DEBUG=False
 5. Configure o serviço de email
 6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
#configure email
git push heroku master --force
```
