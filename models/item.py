from extensions import db


class Item(db.Model):
    __tablename__ = 'item'

    item_id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Numeric(asdecimal=True, precision=18, scale=2), nullable=False)

    @classmethod
    def get_all(cls):
        return cls.query.all()
