from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.item import Item
from schema.item import ItemSchema

item_schema = ItemSchema()
item_list_schema = ItemSchema(many=True)


class ItemListResource(Resource):
    def get(self):
        items = Item.get_all()
        # data = []

        # for item in items:
        #     data.append(item.data())

        # return {'data': data}, HTTPStatus.OK
        return item_list_schema.dump(items), HTTPStatus.OK
