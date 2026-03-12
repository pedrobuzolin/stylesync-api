from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from app.database import get_db
from app.models.sale import Sale
from app.decorators import token_required
import io
import csv

sales_bp = Blueprint('sales_bp', __name__)

# RF: O sistema deve permitir a importacao de vendas atraves de um arquivo
@sales_bp.route('/sales/upload', methods=['POST'])
@token_required
def upload_sales(token):
    """
    Importa vendas a partir de um arquivo CSV
    ---
    tags:
      - Vendas
    security:
      - BearerAuth: []
    consumes:
      - multipart/form-data
    parameters:
      - name: file
        in: formData
        type: file
        required: true
        description: Arquivo CSV contendo os dados das vendas
    responses:
      200:
        description: Upload realizado com sucesso
        schema:
          type: object
          properties:
            message:
              type: string
            vendas importadas:
              type: number
            erros encontrados:
              type: array
              items:
                type: string
      400:
        description: Arquivo inválido ou não enviado
    """
    db = get_db()

    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "Nenhum arquivo selecionado"}), 404
    
    if file and file.filename.endswith('.csv'):
        csv_stream = io.StringIO(file.stream.read().decode('UTF-8'), newline=None)
        csv_reader = csv.DictReader(csv_stream)

        sales_to_insert = []
        errors = []

        for num_row, row in enumerate(csv_reader, 1):
            try:
                sale_data = Sale(**row)
                sales_to_insert.append(sale_data.model_dump())
            except ValidationError:
                errors.append(f'Linha {num_row} contem dados invalidos')
            except Exception:
                errors.append(f'Linha {num_row} com erro inesperado nos dados')
    else:
        return jsonify({"error": "Arquivo deve ser CSV"}), 400

    if sales_to_insert:
        try:
            db.sales.insert_many(sales_to_insert)
        except Exception as e:
            return jsonify({"error": f'{e}'})
    return jsonify({
        "message": "Upload realizado com sucesso!",
        "vendas importadas": len(sales_to_insert),
        "erros encontrados": errors
    }), 200