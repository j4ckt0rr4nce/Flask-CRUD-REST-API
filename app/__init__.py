from flask_restx import Api
from .main import app
from .main.controller.person_controller import api as person_ns
from .main.controller.company_controller import api as company_ns
from .main.controller.address_controller import api as address_ns
from .main.controller.order_controller import api as order_ns
from .main.controller.item_controller import api as item_ns




authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    app,
    title='FLASK RESTPLUS(RESTX) API BOILER-PLATE WITH JWT',
    version='1.0',
    description='a boilerplate for flask restplus (restx) web service',
    authorizations=authorizations,
    security='apikey'
)

api.add_namespace(person_ns, path="/person")
api.add_namespace(company_ns, path="/company")
api.add_namespace(address_ns, path="/address")
api.add_namespace(order_ns, path='/order')
api.add_namespace(item_ns, path='/item')


