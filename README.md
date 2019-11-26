# busgv_bot

Bot do Telegram que informa os horários de saída dos ônibus da Grande Vitória - ES

## Instalação do Serverless Framework

```shell
# Instalando serverless
# Necessário Node
sudo npm install serverless -g

# Instalando autocomplete
sls config tabcompletion install

# instalando plugin do python
sls plugin install -n serverless-python-requirements
```

## Ambiente de DEV

```shell
# Pipenv
pipenv install --dev
```

## Deploy

```shell
# Criar arquivo .env com base em .env.default
# Indicar o valor das variáveis
cp .env.default .env

# Pipenv
pipenv shell

# Deploy na AWS
sls deploy

# Excluir deploy
sls remove
```

## Telegram

```shell
# Registrar webhook
curl https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/setWebHook?url=<ENDPOINT_AWS>
```

## Comandos úteis

```shell
# Testar função na AWS
sls invoke -f <function>

# Testar função localmente
sls invoke local -f <function>

# Lint
pylint funcs/*
```
