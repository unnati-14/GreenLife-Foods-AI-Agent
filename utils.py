# utils.py

def update_inventory(products, product_id, quantity):
    """
    Reduces the quantity of the ordered product in inventory stored in session state.
    Returns True if the order can be fulfilled, False if not enough stock.
    """
    product = next((p for p in products if p["id"] == product_id), None)
    if product and product["quantity_available"] >= quantity:
        product["quantity_available"] -= quantity
        return True
    return False

def add_order_to_conversation_history(conversation_history, products, orders):
    """
    Adds order details to the conversation history.
    """
    order_details = "Order Summary:\n"
    for order in orders:
        order_details += f"{order['quantity']} x {order['product']['name']} - Price: ${order['product']['price']:.2f} each\n"
    
    order_details += f"**Total Cost: ${sum(order['product']['price'] * order['quantity'] for order in orders):.2f}**\n"
    
    return conversation_history + "\n" + order_details