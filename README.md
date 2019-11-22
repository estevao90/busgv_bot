# busgv_bot

Bot do Telegram que informa os horários de saída dos ônibus da Grande Vitória - ES

## Instalação do Serverless Framework

```shell
# Instalando serverless
# Necessário Node
sudo npm install serverless -g

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

# Testar função
sls invoke -f <function>

# Excluir deploy
sls remove
```
