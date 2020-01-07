"""
Realiza o processamento de uma mensagem recebida pelo bot
"""
from app import telegram_proxy


class ProcessadorMensagem:
    __STATUS_OK = 200
    __STATUS_BAD_REQUEST = 400
    __STATUS_INTERNAL_ERROR = 500

    def __init__(self, mensagem):
        self.mensagem = mensagem
        self.telegram_proxy = telegram_proxy.TelegramProxy()

        self.obj_msg = None
        self.status_processamento = None

    def __enviar_mensagem(self, mensagem):
        status = self.telegram_proxy.enviar_mensagem(
            mensagem, self.obj_msg['chat']['id'])

        if status:
            self.status_processamento = self.__STATUS_OK
        else:
            self.status_processamento = self.__STATUS_INTERNAL_ERROR

    def processar(self):
        if 'message' in self.mensagem:
            self.obj_msg = self.mensagem['message']
            self.__enviar_mensagem(
                'Sei: *{}*'.format(self.obj_msg['text']))
        else:
            self.status_processamento = self.__STATUS_BAD_REQUEST

    def get_resultado(self):
        resultado = {
            'statusCode': self.status_processamento
        }
        return resultado
