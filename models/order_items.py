from extensions import db


class OrderItem(db.Model):
    __tablename__ = 'order_items'

    order_item_id = db.Column(db.BigInteger, primary_key=True)
    # order_id = db.Column(db.BigInteger, nullable=True)
    # item_id = db.Column(db.Integer, nullable=True)
    order_id = db.Column(db.BigInteger, db.ForeignKey("order.order_id"))
    item_id = db.Column(db.BigInteger,  db.ForeignKey("item.item_id"))
    quantity = db.Column(db.Integer, nullable=True)

    @classmethod
    def get_all(cls):
        return cls.query.all()