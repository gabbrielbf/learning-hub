from flask import Flask, jsonify
from repository.database import db

app = Flask(__name__)

db.init_app(app)

# Rota responsável por criar o registro de pagamento dentro do banco 
# de dados e retonar ao usuário as informações o específico registro
@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():
    return jsonify({
        'message': 'The payment has been created'
    })

# Rota responsável por dar uma porta a uma instituição 
# financeira que recebeu o pagamento foi recebido ou não
@app.route('/payments/pix/confirmation', methods=['POST'])
def pix_confirmation():
    return jsonify({
        'message': 'The payment has been confirmed'
    })

# Rota com metodologia simples, apenas permitir que o usuário visualize 
# o QR code de pagamento, realizar o pagamento em si e saber se o mesmo foi confirmado
@app.route('/payments/pix/<int:payment_id>', methods=['GET']) # <- o payment_id nada mais é que o identificador do pagamento criado na primeira rota
def payment_pix_page(payment_id):
    return 'pagamento via pix'

if __name__ == '__main__':
    app.run(debug=True)