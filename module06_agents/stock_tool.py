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
