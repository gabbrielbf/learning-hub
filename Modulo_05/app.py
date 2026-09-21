from flask import Flask, jsonify, request
from repository.database import db
from models.payment import Payment
from datetime import datetime, timedelta
import os
from payments.pix import Pix

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    os.path.dirname(__file__),
    'instance',
    'database.db'
)
app.config['SECRET_KEY'] = 'SECRET_KEY_WEBSOCKET'
db.init_app(app)

with app.app_context():
    db.create_all()

# Rota responsável por criar o registro de pagamento dentro do banco 
# de dados e retonar ao usuário as informações o específico registro
@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():

    data = request.get_json()

    if 'value' not in data:
        return jsonify({
            'message': 'Invalid value'
        }), 400

    expiration_date = datetime.now() + timedelta(minutes=30)
    new_payment = Payment(value=data['value'], expiration_date=expiration_date)

    pix = Pix()
    data_payment_pix = pix.create_payment()
    
    db.session.add(new_payment)
    db.session.commit()

    return jsonify({
        'message': 'The payment has been created',
        'payment': new_payment.dict()
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