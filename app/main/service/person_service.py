from .. import db
from ..model.customer import Customer, Person, Company
from sqlalchemy.orm import with_polymorphic


customer_manager = with_polymorphic(Customer, [Person, Company])


def create_person(data):
    customer = Person(**data)

    customer.id = data.get('id')
    customer.phone_number = data.get('phone_number')
    customer.email_address = data.get('email_address')
    customer.customer_type = data.get('customer_type')
    customer.first_name = data.get('first_name')
    customer.last_name = data.get('last_name')
    customer.date_of_birth = data.get('date_of_birth')


    db.session.add(customer)
    db.session.commit()


def get_persons():
    return Person.query.all()

def get_a_person(customer_id):
    return Person.query.get(customer_id)


def update_person(customer_id, data):
    customer = Person.query.filter(Customer.id == customer_id).one()

    customer.id = data.get('id')
    customer.phone_number = data.get('phone_number')
    customer.email_address = data.get('email_address')
    customer.customer_type = data.get('customer_type')
    customer.first_name = data.get('first_name')
    customer.last_name = data.get('last_name')
    customer.date_of_birth = data.get('date_of_birth')

    db.session.add(customer)
    db.session.commit()


def delete_person(customer_id):
    customer = Customer.query.get(customer_id)
    db.session.delete(customer)
    db.session.commit()