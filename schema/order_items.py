from marshmallow import Schema, fields, post_dump, validate, validates, ValidationError

from schema.item import ItemSchema


class OrderItemSchema(Schema):
    class Meta:
        ordered = True

    order_item_id = fields.Int()
    order_id = fields.Int(required=True)
    item_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
    items = fields.Nested(ItemSchema, attribute='item', dump_only=True,
                          only=['name', 'price'])
