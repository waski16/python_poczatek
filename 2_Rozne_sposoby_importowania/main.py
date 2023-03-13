
from shop.orders import create_new_order

def run_shop():
    print("Witaj w naszym sklepie!")
    product_name = input("Podaj nazwę produktu: ")
    quantity = int(input("Podaj ilość: "))

    result = create_new_order(product_name, quantity)
    if result is not None:
        total_price = result["total_price"]
        print(f"Łączny koszt zamówienia: {total_price} PLN.")


if __name__ == '__main__':
    run_shop()
