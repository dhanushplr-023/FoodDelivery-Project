from flask import Flask, render_template, request
import boto3
import json
from datetime import datetime

app = Flask(__name__)

# Replace this with your actual SQS Queue URL
QUEUE_URL = "https://sqs.ap-south-1.amazonaws.com/766265104797/food-orders-queue"

# Create SQS client
sqs = boto3.client("sqs", region_name="ap-south-1")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/order", methods=["POST"])
def order():

    customer_name = request.form.get("customer_name")
    customer_email = request.form.get("customer_email")
    food_item = request.form.get("food_item")
    quantity = request.form.get("quantity")

    order_data = {
    "customer_name": customer_name,
    "customer_email": customer_email,
    "food_item": food_item,
    "quantity": quantity,
    "status": "Pending",
    "order_time": datetime.utcnow().isoformat()
    }

    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(order_data)
    )

    return f"""
    <h2>✅ Order Sent Successfully!</h2>

    <p><b>Customer:</b> {customer_name}</p>

    <p><b>Food Item:</b> {food_item}</p>

    <br>

    <a href="/">Place Another Order</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
