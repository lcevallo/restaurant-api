from extensions import db


class OrderItem(db.Model):
    __tablename__ = 'order_items'

    order_item_id = db.Column(db.BigInteger, primary_key=True)
    # order_id = db.Column(db.BigInteger, nullable=True)
    # item_id = db.Column(db.Integer, nullable=True)
    order_id = db.Column(db.BigInteger, db.ForeignKey("order.order_id"))
    item_id = db.Column(db.BigInteger, db.ForeignKey("item.item_id"))
    quantity = db.Column(db.Integer, nullable=True)

    # Relationships
    item = db.relationship('Item', backref='order_items')

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(order_item_id=id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
