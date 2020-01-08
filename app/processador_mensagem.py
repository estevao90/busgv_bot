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

        self.status_processamento = self.__STATUS_OK
        self.obj_msg = None

    def __responder_chat(self, mensagem):
        status = self.telegram_proxy.enviar_mensagem(
            mensagem, self.obj_msg['chat']['id'])

        if not status:
            self.status_processamento = self.__STATUS_INTERNAL_ERROR

    def __exibir_ajuda(self):
        mensagem_ajuda = '''
*\U0001F68C @busgv_bot*

Horário de partida dos ônibus que circulam na Grande Vitória, ES, Brasil.
A fonte dos dados é o site da [CETURB/ES](https://ceturb.es.gov.br).

*\U0001F449 Instruções:*
Para saber os próximos 3 horários de partida, envie o número da linha, ex:
`809`
`1802`

*\U0001F4D6 Código-fonte:*
https://github.com/estevao90/busgv\_bot

    '''
        self.__responder_chat(mensagem_ajuda)

    def __processar_comando(self):
        if (self.obj_msg['text'] == '/start'
                or self.obj_msg['text'] == '/ajuda'):
            self.__exibir_ajuda()
        else:
            self.__responder_chat(
                'Ops, comando inválido. Para mais detalhes, utilize a /ajuda.')

    def processar(self):
        if 'message' in self.mensagem:
            self.obj_msg = self.mensagem['message']

            # Caso de ser um comando
            if ('entities' in self.obj_msg and
                    self.obj_msg['entities'][0]['type'] == 'bot_command'):
                self.__processar_comando()

        else:
            self.status_processamento = self.__STATUS_BAD_REQUEST

    def get_resultado(self):
        resultado = {
            'statusCode': self.status_processamento
        }
        return resultado
