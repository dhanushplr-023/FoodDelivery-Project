import json
import os
import boto3
import logging

dynamodb = boto3.resource("dynamodb")
sns = boto3.client("sns")

TABLE_NAME = os.environ["TABLE_NAME"]
SNS_TOPIC_ARN = os.environ["SNS_TOPIC_ARN"]

table = dynamodb.Table(TABLE_NAME)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    for record in event["Records"]:

        message = json.loads(record["body"])
        logger.info("===== New Order Received =====")
        logger.info(json.dumps(message, indent=4))

        order_id = message["order_id"]
        customer_name = message["customer_name"]
        phone_number = message["phone_number"]
        delivery_address = message["delivery_address"]
        food_item = message["food_item"]
        quantity = message["quantity"]
        special_instructions = message["special_instructions"]
        status = message["status"]
        order_time = message["order_time"]

        table.put_item(
            Item={
                "order_id": order_id,
                "customer_name": customer_name,
                "phone_number": phone_number,
                "delivery_address": delivery_address,
                "food_item": food_item,
                "quantity": quantity,
                "special_instructions": special_instructions,
                "status": status,
                "order_time": order_time
            }
        )
        logger.info(f"Order {order_id} saved to DynamoDB.")

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="🍔 New Food Order Received",
            Message=f"""
Food Order Confirmation

Order ID: {order_id}

Customer Name: {customer_name}

Phone Number: {phone_number}

Delivery Address:
{delivery_address}

Food Item: {food_item}

Quantity: {quantity}

Special Instructions:
{special_instructions}

Status: {status}

Order Time:
{order_time}

Thank you for ordering with Foodie Express!
"""
        )
        logger.info(f"SNS notification sent for Order {order_id}.")
        logger.info("Lambda execution completed successfully.")
    return {
        "statusCode": 200,
        "body": "Order processed successfully."
    }
