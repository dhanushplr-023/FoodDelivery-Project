from flask import Flask, render_template, request
import boto3
import json
from datetime import datetime
import uuid

app = Flask(__name__)

# Replace this with your SQS Queue URL
QUEUE_URL = "https://sqs.ap-south-1.amazonaws.com/766265104797/food-orders-queue"

# Create SQS Client
sqs = boto3.client("sqs", region_name="ap-south-1")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/order", methods=["POST"])
def order():

    customer_name = request.form.get("customer_name")
    phone_number = request.form.get("phone_number")
    delivery_address = request.form.get("delivery_address")
    food_item = request.form.get("food_item")
    other_food = request.form.get("other_food")
    quantity = request.form.get("quantity")
    special_instructions = request.form.get("special_instructions")

    # If user selected "Other"
    if food_item == "Other" and other_food:
        food_item = other_food

    order_data = {

        "order_id": str(uuid.uuid4()),

        "customer_name": customer_name,

        "phone_number": phone_number,

        "delivery_address": delivery_address,

        "food_item": food_item,

        "quantity": quantity,

        "special_instructions": special_instructions,

        "status": "Pending",

        "order_time": datetime.utcnow().isoformat()

    }

    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(order_data)
    )

    return f"""
    <h2>✅ Order Placed Successfully!</h2>

    <hr>

    <p><b>Order ID:</b> {order_data['order_id']}</p>

    <p><b>Customer:</b> {customer_name}</p>

    <p><b>Phone:</b> {phone_number}</p>

    <p><b>Food:</b> {food_item}</p>

    <p><b>Quantity:</b> {quantity}</p>

    <p><b>Status:</b> Pending</p>

    <br>

    <a href="/">⬅ Place Another Order</a>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
