from marshmallow import Schema, fields


class ItemSchema(Schema):
    class Meta:
        ordered = True

    item_id = fields.Int(dump_only=True)
    name = fields.String(dump_only=True)
    price = fields.Float(dump_only=True)
