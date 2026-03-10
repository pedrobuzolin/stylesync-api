from flask import Flask
from app.database import init_db

def create_app(testing=False):
    app = Flask(__name__)
    app.config.from_object('config.Config')

    try:
        init_db(app.config['MONGO_URI'], testing)
    except Exception as e:
        print(f'Erro ao realizar a conexao com o banco de dados. {e}')

    from .routes.main import main_bp
    from .routes.user_routes import user_bp
    from .routes.products_routes import products_bp
    from .routes.sales_routes import sales_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(sales_bp)

    return app