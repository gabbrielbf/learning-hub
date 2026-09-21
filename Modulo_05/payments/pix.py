import uuid, qrcode, os

class Pix:
    def __init__(self):
        pass

    def create_payment(self):

        # Criando pagamento na instituição financeira, como não 
        # faremos integração com nenhum banco, os dados serão gerados aqui
        bank_payment_id = str(uuid.uuid4())

        # Criando qr code COPIA e COLA ilusório
        hash_payment = f'hash_payment_{bank_payment_id}'

        # Encontrando o caminho da pasta para gerar arquivo e guardar o qrcode
        basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        image_dir = os.path.join(basedir, 'static', 'img')
        image_path = os.path.join(image_dir, f'qr_code_payment_{bank_payment_id}.png')

        # Criando e salvando imagem em si do qr code
        img = qrcode.make(hash_payment)
        img.save(image_path)

        return {
            'bank_payment_id': bank_payment_id,
            'qr_code_path': f'qr_code_payment_{bank_payment_id}'
        }