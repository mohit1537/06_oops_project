class Product:
    def __init__(self,price):
        self._price = price 

    @property
    def price(self):
        print("Getting Price...")
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be Negative")
        else:
            print("Setting Price...")
            self._price

    @price.deleter
    def price(self):
        print("Deleting Price...")

if __name__ == "__main__":
    p = Product(100)

    print(p.price)

    p.price = 150
    print(p.price)

    p.price = -20

    del p.price

