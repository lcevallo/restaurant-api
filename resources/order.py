from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.order import Order
from schema.order import OrderSchema

order_schema = OrderSchema()
order_list_schema = OrderSchema(many=True)

class OrderListResource(Resource):
    def get(self):
        orders = Order.get_all()
        return order_list_schema.dump(orders).data, HTTPStatus.OK
    
    
    def post(self):

        json_data = request.get_json()
        
        order_json = json_data['order']
        order_items_json = json_data['order_items']

        data, errors = order_schema.load(data=order_json)

        if errors:
            return {'message': 'Validation errors', 'errors': errors}, HTTPStatus.BAD_REQUEST

        order = Order(**data)
        order.save()

        return order_schema.dump(order).data, HTTPStatus.CREATED
