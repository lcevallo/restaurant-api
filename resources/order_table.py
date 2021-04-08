from extensions import db
from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.order_table import OrderTable


class OrderTableListResource(Resource):

    def get(self):
        rs = db.session.execute('''
                                SELECT
                                `order`.order_id,
                                `order`.order_no,
                                customer.name,
                                `order`.p_method,
                                `order`.g_total
                                FROM `order`
                                INNER JOIN customer
                                    ON `order`.customer_id = customer.customer_id
                                    ''')
        data = []

        for row in rs:
            if row:
                orders_table = OrderTable(
                    row['order_id'],
                    row['order_no'],
                    row['name'],
                    row['p_method'],
                    row['g_total']
                )
                data.append(orders_table.data)

        return {'orders_list': data}, HTTPStatus.OK
