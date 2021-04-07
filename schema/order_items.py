from marshmallow import Schema, fields, post_dump, validate, validates, ValidationError


class OrderItemSchema(Schema):
    class Meta:
        ordered = True

    order_item_id = fields.Int(dump_only=True)
    order_id = fields.Int(required=True)
    item_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
