from .. import db


class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    internal_identifier = db.Column(db.Integer, nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(length=150), nullable=False)

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))