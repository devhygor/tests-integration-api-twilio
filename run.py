
import os
from twilio.rest import Client


class Twilio:
    
    def __init__(self) -> None:
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.service = 'VA56da5fba931f015f7573e2effa5608a1'
        self.client = Client(self.account_sid, self.auth_token)
    
    def send_code_to_number(self, cell_phone, type_channel):
        """Envia o codigo para o numero de celular

        Args:
            cell_phone (str): string com o numero de celular ex: +5561999999999
            type_channel (str): serviço que sera usado para enviar o codigo
        """
        verification = self.client.verify \
                            .v2 \
                            .services(self.service) \
                            .verifications \
                            .create(to=cell_phone, channel=type_channel)
        print(verification.sid)
    
    def input_code(self):
        code = input(f'Digite o codigo que recebeu via sms ou whatsapp: ')
        return code

    def validate_code(self, cell_phone, code):
        """Valida o codigo

        Args:
            cell_phone (str): string com o numero de celular ex: +5561999999999
            code (int): codigo valido ex: 1234
        """
        verification_check = self.client.verify \
                           .v2 \
                           .services(self.service) \
                           .verification_checks \
                           .create(to=cell_phone, code=code)
        print(verification_check.status)
        
if __name__ == '__main__':
    cell_phone = os.environ['MEU_NUMERO_CELULAR'] # numero que ira receber o codigo
    twilio = Twilio()
    twilio.send_code_to_number(cell_phone, 'sms')
    code = twilio.input_code()
    twilio.validate_code(cell_phone, code)
    print('Codigo finalizado!')
