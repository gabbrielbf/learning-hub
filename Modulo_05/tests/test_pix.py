import pytest, os, sys
from payments.pix import Pix

sys.path.append('../') # Adicionando tudo que temos na pasta "Modulo_05" para encontrar os caminhos dos arquivos

def test_pix_create_payment():

    pix = Pix()

    # Criando pagamento
    payment_info = pix.create_payment(base_dir='../')

    assert 'bank_payment_id' in payment_info
    assert 'qr_code_path' in payment_info

    qr_code_path = payment_info['qr_code_path']
    assert os.path.isfile(f'../static/img/{qr_code_path}.png')