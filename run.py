from app.main import app
from app.main.model.user import User
from app.main.model.customer import Customer
from app.main.model.address import Address
from app.main.model.order import Order
from app.main.model.item import Item

if __name__ == '__main__':
    app.run(debug=True)
    
from app.main import routes
