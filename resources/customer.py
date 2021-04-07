from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.customer import Customer
from schema.customer import CustomerSchema



customer_schema = CustomerSchema()
customer_list_schema = CustomerSchema(many=True)


class CustomerListResource(Resource):
    def get(self):
        customers = Customer.get_all()
        # data = []

        # for customer in customers:
        #     data.append(customer.data())

        # return {'data': data}, HTTPStatus.OK
        return customer_list_schema.dump(customers), HTTPStatus.OK