from flask import jsonify
from sqlalchemy import desc

from app.main import db
from app.main.model.order import Order


def create_order(data):
    order = Order(**data)

    db.session.add(order)
    db.session.commit()

    return "Success Created"


def get_orders():
    return Order.query.all()


def get_a_order(order_id):
    return Order.query.get(order_id)


def update_order(order_id, data):
    order = Order.query.filter(Order.id == order_id).one()

    order.internal_identifier = data.get('internal_identifier')
    order.total_cost = data.get('total_cost')

    db.session.add(order)
    db.session.commit()


def delete_order(order_id):
    order = Order.query.get(order_id)

    db.session.delete(order)
    db.session.commit()