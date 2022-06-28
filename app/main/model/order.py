from .. import db


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    internal_identifier = db.Column(db.String(100), nullable=False, unique=True)
    total_cost = db.Column(db.Float, nullable=False)

    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    items = db.relationship('Item', backref='item_order', lazy='dynamic')

    def __repr__(self):
        return f"<Order {self.internal_identifier}>"