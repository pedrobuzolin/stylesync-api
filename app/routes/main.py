from flask import Blueprint, jsonify, request, current_app
from datetime import datetime, timedelta, timezone
from pydantic import ValidationError
from app.database import get_db
import jwt


main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
    return jsonify({'message': 'Bem vindo ao StyleSync!'})

# RF: O sistema deve permitir que um usuário se autentique para obter um token
@main_bp.route('/login', methods=['POST'])
def login():
    db = get_db()

    try:
        raw_data = request.get_json()
        user_data = db.users.find_one({"username":raw_data["username"]})

        if not user_data:
            return jsonify ({"error": "Usuario nao encontrado"}), 404
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    except Exception as e:
        return jsonify ({"error": "Erro durante a requisição do dado"}), 500

    if user_data["password"] == raw_data["password"]:
        token = jwt.encode(
            {
                "user_id": user_data["username"],
                "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
            },
            current_app.config['SECRET_KEY'],
            algorithm='HS256'
        )

        return jsonify({"access_token": token}), 200
    
    return jsonify({"error": "Credenciais invalidas"}), 401