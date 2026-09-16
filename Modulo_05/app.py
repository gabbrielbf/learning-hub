from flask import Flask, jsonify

app = Flask(__name__)

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