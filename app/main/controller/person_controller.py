from flask import request
from flask_restx import Resource

from ..service.person_service import *
from ..utility.dto import PersonDto

api = PersonDto.api
_person = PersonDto.person


@api.route('/')
class PersonList(Resource):
    @api.doc('list_of_registered_persons')
    @api.marshal_list_with(_person, envelope='data')
    def get(self):
        """List all registered persons"""
        return get_persons()

    @api.expect(_person, validate=True)
    @api.response(201, 'Person successfully created.')
    @api.doc('create a new person')
    def post(self):
        try:
            data = request.json
            create_person(data=data)
            response_object = {
            'Status': "Success",
            'Message': "Successfully Created",
            'Data': data
        }
            return response_object, 201
        except Exception as e:
            raise e

@api.route('/<customer_id>')
@api.param('customer_id', 'The Person identifier')
@api.response(404, 'Person not found.')
class Person(Resource):
    @api.doc('get a person')
    @api.marshal_with(_person)
    def get(self, customer_id):
        """get a person given its identifier"""
        person = get_a_person(customer_id)
        if not person:
            api.abort(404)
        else:
            return person

    @api.response(204, 'Person successfully updated')
    def put(self, customer_id):
        try:
            data = request.json
            update_person(customer_id, data)
            response_object = {
                'Status': "Success",
                'Message': "Successfully Updated",
                'Data': data
            }
            return response_object
        except Exception as e:
            response_object = {
                'Status': "Fail",
                'Message': str(e),
            }
            return response_object

    @api.response(204, 'Person successfully deleted.')
    def delete(self, customer_id):

        return delete_person(customer_id), 204
