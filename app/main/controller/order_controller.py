from flask import request
from flask_restx import Resource

from ..service.order_service import *
from ..utility.dto import OrderDto

api = OrderDto.api
_order = OrderDto.order

@api.route('/')
class OrderList(Resource):
    @api.doc('list_of_registered_order')
    @api.marshal_list_with(_order, envelope='data')
    def get(self):
        return get_orders()


    @api.expect(_order, validate=True)
    @api.response(201, 'Order successfully created.')
    @api.doc('create a new order')
    def post(self):
        data = request.json
        return create_order(data=data)


@api.route('/<order_id>')
@api.param('order_id', 'The Order identifier')
@api.response(404, 'Order not found.')
class Order(Resource):
    @api.doc('get a order')
    @api.marshal_with(_order)
    def get(self, order_id):
        """get a order given its identifier"""
        order = get_a_order(order_id)
        if not order:
            api.abort(404)
        else:
            return order

    @api.response(204, 'Order successfully updated')
    def put(self, order_id):
        try:
            data = request.json
            update_order(order_id, data)
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

    @api.response(204, 'Order successfully deleted.')
    def delete(self, order_id):
        return delete_order(order_id),204

