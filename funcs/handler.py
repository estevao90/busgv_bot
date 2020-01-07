"""
AWS Lambdas
"""

import json
from app import processador_mensagem


def bot_webhook(event, _):
    if 'body' in event:
        body = json.loads(event['body'])
    else:
        body = event

    processador = processador_mensagem.ProcessadorMensagem(body)
    processador.processar()

    return processador.get_resultado()
