from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.order import Order


class OrderListResource(Resource):
    def get(self):
        orders = Order.get_all()
        data = []

        for order in orders:
            data.append(order.data())

        return {'data': data}, HTTPStatus.OK
