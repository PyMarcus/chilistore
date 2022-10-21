import datetime
import time
from typing import Any
from application import database, app


class Store(database.Model):
    """
    Database model with content
    to sell into store
    """

    __tablename__ = 'products'

    id = database.Column(database.Integer(), primary_key=True)
    product = database.Column(database.String(length=100), nullable=False)
    name = database.Column(database.String(length=50), nullable=False, unique=True)
    barcode = database.Column(database.String(length=20), nullable=False, unique=True)
    price = database.Column(database.Float(), nullable=False)
    description = database.Column(database.String(length=100), nullable=False, unique=True)
    datetime = database.Column(database.DateTime(timezone=True), default=datetime.datetime.now())

    def __repr__(self):
        # represent the instance
        return f"Product: {self.id} - {self.name} - {self.datetime} - R$ {self.price} - {self.description}"

    @classmethod
    def create_table(cls) -> None:
        database.create_all()

    @classmethod
    def select_all_products(cls) -> list:
        for product in database.session.query(Store).all():
            yield product

    @classmethod
    def select_a_specific_product(cls, id_of_item: int) -> Any:
        return database.session.query(Store).get(id_of_item)

    @classmethod
    def insert(cls, **kwargs):
        product = Store(name=kwargs["name"],
                        product=kwargs["product"],
                        barcode=kwargs["barcode"],
                        price=kwargs["price"],
                        description=kwargs["description"]
                        )
        database.session.add(product)
        database.session.commit()

    @classmethod
    def delete_product(cls, id_: int) -> None:
        database.session.execute(f"DELETE FROM products WHERE id = {id_};")
        database.session.commit()


if __name__ == '__main__':
    with app.app_context():
        Store.insert(
            name="Yellow Chill",
            barcode="1111111113",
            price=3.95,
            description="Yellow Chili is a picant food",
            product="yellow"
        )
