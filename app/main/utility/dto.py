
from flask_restx import Namespace, fields


class AddressDto:
    api = Namespace('address', description='address related')
    address = api.model('address', {
        'id': fields.Integer(required=True, description='address id'),
        'street':fields.String(required=True, description='address street'),
        'city':fields.String(required=True, description='address city'),
        'postal_code':fields.String(required=True, description='address postal_code'),
        'is_primary':fields.Boolean(required=True, description='address is_primary'),
        'is_contact':fields.Boolean(required=True, description='address is_contact'),
        'customer_id': fields.Integer(required=True, description='address customer_id'),
    })


class OrderDto:
    api = Namespace('orders', description='orders related')
    order = api.model('orders', {
        'id': fields.Integer(required=True, description='order id'),
        'internal_identifier': fields.String(required=True, description='order internal_identifier'),
        'total_cost': fields.Float(required=True, description='order total_cost'),
        'customer_id': fields.Integer(required=True, description='order customer_id'),

    })


class ItemDto:
    api = Namespace('items', description='items related')
    item = api.model('items', {
        'id': fields.Integer(required=True, description='item id'),
        'internal_identifier': fields.String(required=True, description='item internal_identifier'),
        'price': fields.Float(required=True, description='item price'),
        'description': fields.String(required=True, description='item description'),
        'order_id': fields.Integer(required=True, description='item order_id'),
    })


class PersonDto:
    api = Namespace('person', description='person related')
    person = api.model('person', {
        'id': fields.Integer(required=True, description='person id'),
        'phone_number': fields.Integer(required=True, description='person phone_number'),
        'email_address': fields.String(required=True, description='person email_address'),
        'customer_type': fields.String(required=True, description='person customer_type'),
        'first_name': fields.String(required=True, description='person first_name'),
        'last_name': fields.String(required=True, description='person last_name'),
        'date_of_birth': fields.String(required=True, description='person date_of_birth'),
    })


class CompanyDto:
    api = Namespace('company', description='company related')
    company = api.model('company', {
        'id': fields.Integer(required=True, description='company id'),
        'phone_number': fields.Integer(required=True, description='company phone_number'),
        'email_address': fields.String(required=True, description='company email_address'),
        'customer_type': fields.String(required=True, description='company customer_type'),
        
        'ICO': fields.Integer(required=True, description='company ICO'),
        'DIC': fields.Integer(required=True, description='company DIC'),
    })