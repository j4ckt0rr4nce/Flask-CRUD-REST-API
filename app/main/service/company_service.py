from .. import db
from ..model.customer import Customer, Person, Company
from sqlalchemy.orm import with_polymorphic


customer_manager = with_polymorphic(Customer, [Person, Company])


def create_company(data):
    customer = Company(**data)

    customer.id = data.get('id')
    customer.phone_number = data.get('phone_number')
    customer.email_address = data.get('email_address')
    customer.customer_type = data.get('customer_type')
    customer.ICO = data.get('ICO')
    customer.DIC = data.get('DIC')

    db.session.add(customer)
    db.session.commit()


def get_companies():
    return Company.query.all()

def get_a_company(customer_id):
    return Company.query.get(customer_id)


def update_company(customer_id, data):
    customer = Company.query.filter(Customer.id == customer_id).one()

    customer.id = data.get('id')
    customer.phone_number = data.get('phone_number')
    customer.email_address = data.get('email_address')
    customer.customer_type = data.get('customer_type')
    customer.ICO = data.get('ICO')
    customer.DIC = data.get('DIC')

    db.session.add(customer)
    db.session.commit()


def delete_company(customer_id):
    customer = Customer.query.get(customer_id)
    db.session.delete(customer)
    db.session.commit()