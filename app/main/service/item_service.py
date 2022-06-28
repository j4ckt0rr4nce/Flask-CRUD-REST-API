from .. import db
from ..model.item import Item


def create_item(data):
    item = Item(**data)

    db.session.add(item)
    db.session.commit()

    return "Success Created"


def get_items():
    return Item.query.all()

def get_a_item(item_id):
    return Item.query.get(item_id)


def update_item(item_id, data):
    item = Item.query.filter(Item.id == item_id).one()

    item.internal_identifier = data.get('internal_identifier')
    item.price = data.get('price')
    item.description = data.get('description')

    db.session.add(item)
    db.session.commit()


def delete_item(item_id):
    item = Item.query.get(item_id)
    db.session.delete(item)
    db.session.commit()