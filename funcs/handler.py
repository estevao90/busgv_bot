import os
import json
import requests

URL = 'https://api.telegram.org/bot{}/'.format(
    os.environ['TELEGRAM_BOT_TOKEN'])


def enviar_mensagem(mensagem, chat_id):
    texto = 'Você disse: ' + mensagem
    url = URL + 'sendMessage?text={}&chat_id={}'.format(texto, chat_id)
    requests.get(url, timeout=2)


def bot_webhook(event, context):
    if 'body' in event:
        body = json.loads(event['body'])
    else:
        body = event
    chat_id = body['message']['chat']['id']
    resposta = body['message']['text']
    enviar_mensagem(resposta, chat_id)
    return {
        'statusCode': 200
    }
