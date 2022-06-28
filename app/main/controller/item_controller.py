from flask import request
from flask_restx import Resource

from ..service.item_service import *
from ..utility.dto import ItemDto

api = ItemDto.api
_item = ItemDto.item


@api.route('/')
class ItemList(Resource):
    @api.doc('list_of_registered_item')
    @api.marshal_list_with(_item, envelope='data')
    def get(self):
        """List all registered item"""
        return get_items()

    @api.expect(_item, validate=True)
    @api.response(201, 'Item successfully created.')
    @api.doc('create a new item')
    def post(self):
        try:
            data = request.json
            create_item(data=data)
            response_object = {
            'Status': "Success",
            'Message': "Successfully Created",
            'Data': data
        }
            return response_object, 201
        except Exception as e:
            raise e

@api.route('/<item_id>')
@api.param('item_id', 'The Item identifier')
@api.response(404, 'Item not found.')
class Item(Resource):
    @api.doc('get a item')
    @api.marshal_with(_item)
    def get(self, item_id):
        """get a item given its identifier"""
        item = get_a_item(item_id)
        if not item:
            api.abort(404)
        else:
            return item

    @api.response(204, 'Item successfully updated')
    def put(self, item_id):
        try:
            data = request.json
            update_item(item_id, data)
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

    @api.response(204, 'Item successfully deleted.')
    def delete(self, item_id):

        return delete_item(item_id), 204
