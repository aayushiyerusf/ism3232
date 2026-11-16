# pickup_queue.py
# Author: Aayush Iyer


class PickupQueue:
    """Pickup orders waiting for the barista to approve. Nothing is placed until then."""

    def __init__(self, menu):
        """Start with no requests and no placed orders."""
        self.menu = menu
        self.requests = []
        self.orders = []

    def request_pickup_order(self, customer_name, item):
        """Ask the barista to place a pickup order. The barista must approve it.

        Args:
            customer_name: The customer's name for the order.
            item: One item from the menu, like latte.
        """
        item = item.lower()
        if item not in self.menu:
            return (
                "That item is not on the menu. Ask the customer to choose a menu item."
            )
        number = len(self.requests) + 1
        request = {
            "number": number,
            "customer_name": customer_name,
            "item": item,
            "status": "waiting",
        }
        self.requests.append(request)
        return f"Request {number} was sent to the barista. The order is not placed yet."

    def waiting(self):
        """Return the requests that are still waiting for a decision."""
        result = []
        for request in self.requests:
            if request["status"] == "waiting":
                result.append(request)
        return result

    def find(self, number):
        """Return the request with this number, or None."""
        for request in self.requests:
            if request["number"] == number:
                return request
        return None

    def approve(self, number):
        """Approve one waiting request and place the order."""
        request = self.find(number)
        if request is None:
            return f"There is no request {number}."
        if request["status"] != "waiting":
            return f"Request {number} is already {request['status']}."
        request["status"] = "approved"
        self.orders.append(f"{request['customer_name']}: {request['item']}")
        return f"Request {number} approved."

    def reject(self, number):
        """Reject one waiting request. No order is placed."""
        request = self.find(number)
        if request is None:
            return f"There is no request {number}."
        if request["status"] != "waiting":
            return f"Request {number} is already {request['status']}."
        request["status"] = "rejected"
        return f"Request {number} rejected."
