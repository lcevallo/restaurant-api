from marshmallow import Schema, fields, post_dump, validate, validates, ValidationError
from schema.order_items import OrderItemSchema

class OrderSchema(Schema):
    class Meta:
        ordered = True
        
    order_id = fields.Integer(dump_only=True)
    order_no = fields.String()
    p_method = fields.String()
    g_total = fields.Float()
    customer_id = fields.Integer()
        
    order_items = fields.Nested(OrderItemSchema, attribute='order_items', dump_only=True, only=['order_item_id', 'item_id','quantity'])   