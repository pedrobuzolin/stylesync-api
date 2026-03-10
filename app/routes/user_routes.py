from flask import Blueprint, jsonify, request
from app.models.user import *
from pydantic import ValidationError
from app.database import get_db
from bson import ObjectId
from app.decorators import token_required


user_bp = Blueprint('user_bp', __name__)

# RF: O Sistema deve permitir o usuário listar os usuários cadastrados
@user_bp.route('/users', methods=["GET"])
@token_required
def get_users(token):
    db = get_db()

    try:
        users_cursor = db.users.find({})
        users_list = [UserDBModel(**user).model_dump(by_alias=True, exclude_none=True) for user in users_cursor]
        return jsonify(users_list), 200
    except Exception as e:
        return jsonify({"error": f"Erro ao retornar lista de usuarios."}), 500

# RF: O Sistema deve permitir a criação de novos usuarios
@user_bp.route('/user', methods=["POST"])
def create_user():
    db = get_db()

    try:
        user = User(**request.get_json())
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    
    result = db.users.insert_one(user.model_dump())

    return jsonify({"message": "Usuario cadastrado com sucesso!"}), 201

# RF: O Sistema deve permitir a deleção de usuarios
@user_bp.route('/user/<string:user_id>', methods=["DELETE"])
@token_required
def delete_user_by_id(token, user_id):
    db = get_db()

    try:
        oid = ObjectId(user_id)
    except Exception:
        return jsonify({"error": "Usuario nao encontrado"}), 404
    
    deleted_user = db.users.delete_one({"_id":oid})

    return "", 201