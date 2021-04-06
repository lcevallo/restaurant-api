from extensions import db


class Customer(db.Model):
    __tablename__ = 'customer'

    customer_id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    @classmethod
    def get_all(cls):
        return cls.query.all()