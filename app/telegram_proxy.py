"""
Realiza a interação entre o bot e o Telegram
"""
import os
import requests


class TelegramProxy:
    __TELEGRAM_URL = 'https://api.telegram.org/bot{}/'.format(
        os.environ['TELEGRAM_BOT_TOKEN'])

    @staticmethod
    def enviar_mensagem(mensagem, id_chat):
        try:
            url = TelegramProxy.__TELEGRAM_URL + \
                'sendMessage?text={}&chat_id={}&&parse_mode=markdown'.format(
                    mensagem, id_chat)
            requests.get(url, timeout=2)
            return True
        except requests.exceptions.RequestException:
            return False
