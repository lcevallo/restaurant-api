from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.order_items import OrderItem


class OrderItemListResource(Resource):
    def get(self):
        order_items = OrderItem.get_all()
        data = []

        for order_item in order_items:
            data.append(order_item.data())

        return {'data': data}, HTTPStatus.OK
