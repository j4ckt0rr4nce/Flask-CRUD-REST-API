from .. import db


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.Integer, nullable=False, unique=True)
    email_address = db.Column(db.String(50), nullable=False, unique=True)
    customer_type = db.Column(db.String(50))

    __mapper_args__ = {
        "polymorphic_on": customer_type,
        "polymorphic_identity": "customers",
    }

    

class Person(Customer):
    __tablename__ = None
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    date_of_birth = db.Column(db.String(50))

    __mapper_args__ = {
        "polymorphic_identity": "person",
    }


class Company(Customer):
    __tablename__ = None
    ICO = db.Column(db.Integer, unique=True)
    DIC = db.Column(db.Integer, unique=True)

    __mapper_args__ = {
        "polymorphic_identity": "company",
    }
