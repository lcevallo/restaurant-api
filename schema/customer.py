from marshmallow import Schema, fields


class CustomerSchema(Schema):
    class Meta:
        ordered = True

    customer_id = fields.Int(dump_only=True)
    name = fields.String()