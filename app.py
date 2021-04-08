from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from config import Config
from extensions import db
from resources.customer import CustomerListResource
from resources.item import ItemListResource
from resources.order import OrderListResource, OrderResource
from resources.order_items import OrderItemListResource
from flask_cors import CORS, cross_origin

from resources.order_table import OrderTableListResource


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config[
        'CORS_HEADERS'] = 'Content-Type'  # Le decimos a cors en que formato va a recibir los headers (datos de las peticiones)
    api = Api(app)
    CORS(app)
    cors = CORS(app, resources={
        r"*": {"origins": ["http://localhost:4200", "http://localhost:8000"
                           ]}})  # Permitimos el origen de nuestro servidor local de frontend

    register_extensions(app)
    register_resources(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)


def register_resources(app):
    api = Api(app)
    api.add_resource(CustomerListResource, '/customers')
    api.add_resource(ItemListResource, '/items')
    api.add_resource(OrderListResource, '/orders')
    api.add_resource(OrderItemListResource, '/order-items')
    api.add_resource(OrderTableListResource, '/table-orders')
    api.add_resource(OrderResource, '/orders/<int:order_id>')


if __name__ == '__main__':
    app = create_app()
    app.run()
