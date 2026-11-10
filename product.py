class Product:
    """Product class for seminar 8 activity"""
    def __init__(self, name="", price=0.0):
        """Initialise a product"""
        self.name = name
        self.price = price

    def __str__(self):
        """Return a string representation of a product"""
        return f"{self.name}, ${self.price}"