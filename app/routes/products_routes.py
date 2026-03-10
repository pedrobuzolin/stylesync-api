from flask import Blueprint, jsonify, request, current_app
from pydantic import ValidationError
from app.database import get_db
from bson import ObjectId
from app.models.products import *
from app.decorators import token_required

products_bp = Blueprint('products_bp', __name__)


# RF: O sistema deve permitir a listagem de todos os produtos
@products_bp.route('/products', methods=['GET'])
def get_products():
    db = get_db()
    products_cursor = db.products.find({})
    products_list = [ProductDBModel(**product).model_dump(by_alias=True, exclude_none=True) for product in products_cursor]
    return jsonify(products_list)

# RF: O sistema deve permitir a criação de um novo produto
@products_bp.route('/products', methods=['POST'])
@token_required
def create_product(token):
    db = get_db()

    try:
        product = Product(**request.get_json())
    except ValidationError as e:
        return jsonify({"error": e.errors()})
    
    result = db.products.insert_one(product.model_dump())

    return jsonify({"message": "Produto cadastrado com sucesso!", "id": str(result.inserted_id)}), 201

# RF: O sistema deve permitir a visualização dos detalhes de um único produto
@products_bp.route('/product/<string:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    db = get_db()

    try:
        oid = ObjectId(product_id)
    except Exception as e:
        jsonify({"error": f"Erro ao transformar o {product_id}"})
    
    product = db.products.find_one({"_id": oid})

    if product:
        product_model = ProductDBModel(**product).model_dump(by_alias=True, exclude_none=True)
        return jsonify(product_model)
    else:
        return jsonify({"error": f"Produto com o ID:{product_id} - Não Encontrado"})

# RF: O sistema deve permitir a atualização de um unico produto e produto existente
@products_bp.route('/product/<string:product_id>', methods=['PUT'])
@token_required
def update_product_by_id(token, product_id):
    db = get_db()

    try:
        oid = ObjectId(product_id)
        update_data = UpdateProduct(**request.get_json())

    except ValidationError as e:
        return jsonify({"error": e.errors()})
    
    update_result = db.products.update_one(
        {"_id": oid},
        {"$set": update_data.model_dump(exclude_unset=True)}
    )

    if update_result.matched_count == 0:
        return jsonify({"error": "Produto nao encontrado"}), 404
    
    updated_product = db.products.find_one({"_id": oid})
    return jsonify(ProductDBModel(**updated_product).model_dump(by_alias=True, exclude=None))

# RF: O sistema deve permitir a delecao de um unico produto e produt existente
@products_bp.route('/product/<string:product_id>', methods=['DELETE'])
@token_required
def delete_product_by_id(token, product_id):
    db = get_db()

    try:
        oid = ObjectId(product_id)

    except Exception:
        return jsonify({"error": "ID do produto inválido"}), 400
    
    deleted_product = db.products.delete_one({"_id":oid})

    if deleted_product.deleted_count == 0:
        return jsonify({"error": "Produto nao encontrado"}), 404
    
    return "", 204