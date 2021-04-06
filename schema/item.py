from marshmallow import Schema, fields


class ItemSchema(Schema):
    class Meta:
        ordered = True

    item_id = fields.Int(dump_only=True)
    name = fields.String()
    price = fields.Float()
