from flask import request
from flask_restx import Resource

from ..service.address_service import *
from ..utility.dto import AddressDto

api = AddressDto.api
_address = AddressDto.address

@api.route('/')
class AddressList(Resource):
    @api.doc('list_of_registered_address')
    @api.marshal_list_with(_address, envelope='data')
    def get(self):
        return get_addresses()


    @api.expect(_address, validate=True)
    @api.response(201, 'Address successfully created.')
    @api.doc('create a new address')
    def post(self):
        data = request.json
        return create_address(data=data)


@api.route('/<address_id>')
@api.param('address_id', 'The Address identifier')
@api.response(404, 'Address not found.')
class Address(Resource):
    @api.doc('get a address')
    @api.marshal_with(_address)
    def get(self, address_id):
        """get a address given its identifier"""
        address = get_a_address(address_id)
        if not address:
            api.abort(404)
        else:
            return address

    @api.response(204, 'Address successfully updated')
    def put(self, address_id):
        try:
            data = request.json
            update_address(address_id, data)
            response_object = {
                'Status': "Success",
                'Message': "Successfully Updated",
                'Data': data
            }
            return response_object, 200
        except Exception as e:
            response_object = {
                'Status': "Fail",
                'Message': str(e),
            }
            return response_object,409

    @api.response(204, 'Address successfully deleted.')
    def delete(self, address_id):
        return delete_address(address_id),204