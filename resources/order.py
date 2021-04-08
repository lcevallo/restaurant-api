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
        deleted_order_items_id = json_data['deletedOrderItemsIDs']

        data, errors = order_schema.load(data=json_data)

        if errors:
            return {'message': 'Validation errors', 'errors': errors}, HTTPStatus.BAD_REQUEST

        if data.get('order_id') != 0:
            order = Order.get_by_id(id=data.get('order_id'))
            order.order_no = data.get('order_no') or order.order_no
            order.p_method = data.get('description') or order.description
            order.g_total = data.get('num_of_servings') or order.num_of_servings
            order.customer_id = data.get('customer_id') or order.customer_id
        else:
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

                if data_order_item.get('order_item_id') != 0:
                    order_item = OrderItem.get_by_id(id=data_order_item.get('order_item_id'))
                    order_item.order_id = data.get('order_no') or order_item.order_no
                    order_item.item_id = data.get('description') or order_item.description
                    order_item.quantity = data.get('num_of_servings') or order_item.num_of_servings

                else:
                    order_item = OrderItem(**data_order_item)
                    order_item.order_id = order.order_id

                order_item.save()

            # Delete operations for orders_items

        # order = Order.get_by_id(order.order_id)

        return order_schema.dump(order).data, HTTPStatus.CREATED


class OrderResource(Resource):
    def get(self, order_id):
        order = Order.get_by_id(id=order_id)

        if order is None:
            return {'message': 'Order not found'}, HTTPStatus.NOT_FOUND

        return order_schema.dump(order).data, HTTPStatus.OK
