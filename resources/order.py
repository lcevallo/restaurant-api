from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.order import Order
from models.order_items import OrderItem
from schema.order import OrderSchema
from schema.order_items import OrderItemSchema

order_schema = OrderSchema()
order_list_schema = OrderSchema(many=True)
order_item_schema = OrderItemSchema()


class OrderListResource(Resource):
    def get(self):
        orders = Order.get_all()
        return order_list_schema.dump(orders).data, HTTPStatus.OK

    def post(self):

        json_data = request.get_json()
        order_items_json = json_data['order_items']

        data, errors = order_schema.load(data=json_data)

        if errors:
            return {'message': 'Validation errors', 'errors': errors}, HTTPStatus.BAD_REQUEST

        order = Order(**data)

        # for items in order_items_json:
        #     order.order_items.append(items)

        order.save()

        if order.order_id:
            for item in order_items_json:
                data_order_item, errors_order_item = order_item_schema.load(data=item)                
                if errors:
                    return {'message': 'Validation Order Items Errors',
                            'errors': errors_order_item}, HTTPStatus.BAD_REQUEST

                order_item = OrderItem(**data_order_item)
                order_item.order_id = order.order_id
                order_item.save()

        # order = Order.get_by_id(order.order_id)

        return order_schema.dump(order).data, HTTPStatus.CREATED
