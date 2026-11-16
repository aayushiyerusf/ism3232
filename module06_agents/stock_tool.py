# stock_tool.py
# Author: Aayush Iyer


class StockLookup:  # Define a tool for looking up product stock.
    def __init__(self, stock):  # Accept a dictionary of products and counts.
        self.stock = stock  # Store the dictionary on this tool.

    def find_product(self, text):  # Find a known product in a message.
        for product in self.stock:  # Check each product in dictionary order.
            if product.lower() in text.lower():  # Match without case sensitivity.
                return product  # Return the first matching product.
        return None  # Indicate that no known product was found.

    def count_for(self, product):  # Look up one product's stock count.
        return self.stock.get(product)  # Return its count, or None if unknown.

    def check_stock(self, item):
        """Check how many of one product are in stock.

        Args:
            item: The product name, like rain jacket.
        """
        product = self.find_product(item)
        if product is None:
            return "That product was not found."
        return f"We have {self.count_for(product)} of the {product} in stock."
