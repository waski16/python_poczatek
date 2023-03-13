
from .products_store import products, update_product_quantity


def create_new_order(product_name, quantity):
    if products[product_name]["quantity"] < quantity:
        print("Nie mamy tyle na stanie.")
        return None

    total_price = products[product_name]["price"] * quantity
    new_order = {
        "product": product_name,
        "quantity": quantity,
        "total_price": total_price
    }
    update_product_quantity(product_name, quantity)
    return new_order



