from extensions import db


class Order(db.Model):
    __tablename__ = 'order'

    order_id = db.Column(db.BigInteger, primary_key=True)
    order_no = db.Column(db.String(50), nullable=False)
    # customer_id = db.Column(db.Integer, nullable=False)
    p_method = db.Column(db.String(50), nullable=True)
    g_total = db.Column(db.Numeric(asdecimal=True, precision=18, scale=2), nullable=False)

    customer_id = db.Column(db.BigInteger, db.ForeignKey("customer.customer_id"))

    @classmethod
    def get_all(cls):
        return cls.query.all()
