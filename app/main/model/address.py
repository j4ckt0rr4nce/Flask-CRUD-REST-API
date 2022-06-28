from .. import db


class Address(db.Model):
    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(length=50), nullable=False)
    postal_code = db.Column(db.String(50), nullable=False)
    is_primary = db.Column(db.Boolean, nullable=True, default=False)
    is_contact = db.Column(db.Boolean, nullable=True, default=False)

    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))