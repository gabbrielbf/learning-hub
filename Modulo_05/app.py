from flask import Flask, jsonify

app = Flask(__name__)

# Rota responsável por criar o registro de pagamento dentro do banco 
# de dados e retonar ao usuário as informações o específico registro
@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():
    return jsonify({
        'message': 'The payment has been created'
    })