# busgv_bot

Bot do Telegram que informa os horários de saída dos ônibus da Grande Vitória - ES

## Instalação do Serverless Framework

```shell
# Instalando serverless
# Necessário Node
sudo npm install serverless -g

# instalando plugin do python
sls plugin install -n serverless-python-requirements

# Instalando autocomplete
sls config tabcompletion install
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

# Verificar status do webhook
curl https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/getWebhookInfo
```

## Desenvolvimento

```shell
# Remover webhook
curl https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/deleteWebhook

# Obtendo mensagens
curl https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/getUpdates

# Para obter apenas as novas mensagens
curl https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/getUpdates?offset=<result[-1].update_id + 1>
```

## Comandos úteis

```shell
# Testar função na AWS
sls invoke -f <function> [-p <event_file_path> -x <context_file_path>]

# Testar função localmente
sls invoke local -f <function> [-p <event_file_path> -x <context_file_path>]

# Lint
pylint funcs/*
```
