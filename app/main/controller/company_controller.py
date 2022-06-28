from flask import request
from flask_restx import Resource

from ..service.company_service import *
from ..utility.dto import CompanyDto

api = CompanyDto.api
_company = CompanyDto.company


@api.route('/')
class CompanyList(Resource):
    @api.doc('list_of_registered_companies')
    @api.marshal_list_with(_company, envelope='data')
    def get(self):
        """List all registered companies"""
        return get_companies()

    @api.expect(_company, validate=True)
    @api.response(201, 'Company successfully created.')
    @api.doc('create a new company')
    def post(self):
        try:
            data = request.json
            create_company(data=data)
            response_object = {
            'Status': "Success",
            'Message': "Successfully Created",
            'Data': data
        }
            return response_object, 201
        except Exception as e:
            raise e

@api.route('/<customer_id>')
@api.param('customer_id', 'The Company identifier')
@api.response(404, 'Company not found.')
class Company(Resource):
    @api.doc('get a company')
    @api.marshal_with(_company)
    def get(self, customer_id):
        """get a company given its identifier"""
        company = get_a_company(customer_id)
        if not company:
            api.abort(404)
        else:
            return company

    @api.response(204, 'Company successfully updated')
    def put(self, customer_id):
        try:
            data = request.json
            update_company(customer_id, data)
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

    @api.response(204, 'Company successfully deleted.')
    def delete(self, customer_id):

        return delete_company(customer_id), 204
