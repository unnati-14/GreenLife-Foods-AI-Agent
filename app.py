# app.py

import streamlit as st
from llama_model import query_llama
from utils import update_inventory, add_order_to_conversation_history

# -------------------------------
# Page configuration & Title
# -------------------------------
st.set_page_config(page_title="GreenLife Foods Order Chatbot", layout="wide")
st.title("GreenLife Foods Order Capture Chatbot")

# -------------------------------
# Product Catalog
# -------------------------------
# Define at least 10 products. Each product has an id, name, price, and description.
if "products" not in st.session_state:
    st.session_state.products = [
    {"id": "1", "name": "Organic Apple Juice", "price": 3.50, "description": "Freshly squeezed apple juice made from organic apples.", "quantity_available": 10},
    {"id": "2", "name": "Organic Almond Butter", "price": 7.00, "description": "Smooth almond butter made from organic almonds.", "quantity_available": 5},
    {"id": "3", "name": "Organic Granola", "price": 5.00, "description": "Healthy granola made with organic oats and honey.", "quantity_available": 8},
    {"id": "4", "name": "Organic Chia Seeds", "price": 4.50, "description": "Nutritious chia seeds sourced organically.", "quantity_available": 12},
    {"id": "5", "name": "Organic Honey", "price": 6.00, "description": "Pure organic honey.", "quantity_available": 6},
    {"id": "6", "name": "Organic Green Tea", "price": 4.00, "description": "Refreshing organic green tea.", "quantity_available": 10},
    {"id": "7", "name": "Organic Dark Chocolate", "price": 3.00, "description": "Rich dark chocolate made from organic cacao.", "quantity_available": 7},
    {"id": "8", "name": "Organic Quinoa", "price": 8.00, "description": "Protein-packed organic quinoa.", "quantity_available": 4},
    {"id": "9", "name": "Organic Extra Virgin Olive Oil", "price": 12.00, "description": "Cold-pressed olive oil from organic olives.", "quantity_available": 3},
    {"id": "10", "name": "Organic Coconut Water", "price": 2.50, "description": "Refreshing organic coconut water.", "quantity_available": 15},
    {"id": "11", "name": "Organic Avocado Oil", "price": 10.00, "description": "Cold-pressed organic avocado oil.", "quantity_available": 5},
    {"id": "12", "name": "Organic Brown Rice", "price": 6.50, "description": "Whole grain brown rice grown organically.", "quantity_available": 9},
    {"id": "13", "name": "Organic Cashews", "price": 9.00, "description": "Raw organic cashews, rich in healthy fats.", "quantity_available": 6},
    {"id": "14", "name": "Organic Matcha Powder", "price": 11.00, "description": "High-quality organic matcha for lattes and smoothies.", "quantity_available": 8},
    {"id": "15", "name": "Organic Dried Mango", "price": 7.50, "description": "Naturally sweet dried mango with no added sugar.", "quantity_available": 7},
    {"id": "16", "name": "Organic Walnuts", "price": 8.50, "description": "Raw organic walnuts, great for snacking and baking.", "quantity_available": 5},
    {"id": "17", "name": "Organic Oat Milk", "price": 4.25, "description": "Creamy organic oat milk, dairy-free.", "quantity_available": 10},
    {"id": "18", "name": "Organic Chickpeas", "price": 3.75, "description": "Protein-rich organic chickpeas for cooking.", "quantity_available": 12},
    {"id": "19", "name": "Organic Peanut Butter", "price": 6.25, "description": "Smooth organic peanut butter with no added sugar.", "quantity_available": 4},
    {"id": "20", "name": "Organic Cacao Nibs", "price": 7.80, "description": "Raw organic cacao nibs for baking and smoothies.", "quantity_available": 6}
]


# -------------------------------
# Initialize Session State Variables
# -------------------------------
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = ""
    product_catalog_info = "Our product catalog includes the following items:\n"
    for product in st.session_state.products:
        product_catalog_info += f"**{product['name']}** - {product['description']} - Price: ${product['price']:.2f} - Quantiyt: {product['quantity_available']}\n"
    
    st.session_state.conversation_history += product_catalog_info

if "orders" not in st.session_state:
    st.session_state.orders = []

# -------------------------------
# Sidebar: Product Catalog and Order Entry
# -------------------------------
st.sidebar.header("Product Catalog")
for product in st.session_state.products:
    st.sidebar.write(f"{product['id']}. **{product['name']}** - ${product['price']:.2f} - Available: {product['quantity_available']}")
    st.sidebar.caption(product["description"])

st.sidebar.markdown("---")
st.sidebar.header("Place an Order")

# Create a dropdown to select a product (display product id and name)
product_options = [f"{p['id']}. {p['name']}" for p in st.session_state.products]
selected_product = st.sidebar.selectbox("Select Product", product_options)

quantity = st.sidebar.number_input("Quantity", min_value=1, value=1, step=1)

# Button to add product to the order list
if st.sidebar.button("Add to Order"):
    product_id = selected_product.split(".")[0]
    product = next((p for p in st.session_state.products if p["id"] == product_id), None)
    if product:
        if update_inventory(st.session_state.products, product_id, quantity):
            st.session_state.orders.append({"product": product, "quantity": quantity})
            st.session_state.conversation_history = add_order_to_conversation_history(st.session_state.conversation_history, st.session_state.products, st.session_state.orders)
            st.sidebar.success(f"Added {quantity} x {product['name']} to order.")
        else:
            st.sidebar.error(f"Insufficient stock for {product['name']}. Only {product['quantity_available']} units available.")

# Display Order Summary in the sidebar
if st.session_state.orders:
    st.sidebar.subheader("Order Summary")
    total_cost = 0
    for order in st.session_state.orders:
        line_total = order['product']['price'] * order['quantity']
        total_cost += line_total
        st.sidebar.write(f"{order['quantity']} x {order['product']['name']} - ${line_total:.2f}")
    st.sidebar.write(f"**Total: ${total_cost:.2f}**")

# -------------------------------
# Main Chatbot Interface
# -------------------------------
st.header("Chat with the Order Bot")
st.write("Ask about our products, inquire about order status, or get help with placing an order.")

# Display conversation history (optional)
if st.session_state.conversation_history:
    st.text_area("Conversation History", value=st.session_state.conversation_history, height=300)

# Input for chat message
user_input = st.text_input("Your Message:", key="user_input_field")

# When the user clicks 'Send', process the message
if st.button("Send"):
    if user_input:
        # Append the new user message to conversation history.
        st.session_state.conversation_history += f"\nUser: {user_input}"
        # Query the Llama model using our helper function.
        response_text = query_llama(user_input, st.session_state.conversation_history)
        # Append the assistant response to conversation history.
        st.session_state.conversation_history += f"\nAssistant: {response_text}"
        # Display the assistant's response.
        st.write(response_text)
    else:
        st.write("Please enter a message before sending.")