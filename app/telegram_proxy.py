"""
Realiza a interação entre o bot e o Telegram
"""
import os
import urllib.parse
import requests


class TelegramProxy():
    __TELEGRAM_URL = 'https://api.telegram.org/bot{}/'.format(
        os.environ['TELEGRAM_BOT_TOKEN'])

    @staticmethod
    def enviar_mensagem(mensagem, id_chat):
        try:
            url_inicial = TelegramProxy.__TELEGRAM_URL + \
                'sendMessage?parse_mode=markdown&disable_web_page_preview=true&'
            params = {'chat_id': id_chat, 'text': mensagem}
            url = '{}{}'.format(
                url_inicial, urllib.parse.urlencode(params))

            res = requests.get(url, timeout=2)
            return res.status_code == 200
        except requests.exceptions.RequestException:
            return False
