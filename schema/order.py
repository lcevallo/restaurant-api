from marshmallow import Schema, fields, post_dump, validate, validates, ValidationError
from schema.order_items import OrderItemSchema


class OrderSchema(Schema):
    class Meta:
        ordered = True

    order_id = fields.Integer()
    order_no = fields.String()
    p_method = fields.String()
    g_total = fields.Float()
    customer_id = fields.Integer()

    order_items = fields.Nested(OrderItemSchema, many=True, attribute='order_items', dump_only=True, exclude=('order_id',))

    # order_items = fields.Nested(OrderItemSchema, attribute='items', dump_only=True,
    #                      exclude=('order_id',))