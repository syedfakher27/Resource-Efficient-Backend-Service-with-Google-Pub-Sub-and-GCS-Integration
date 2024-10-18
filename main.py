import os
import json
from google.cloud import pubsub_v1
from google.cloud.pubsub_v1.types import FlowControl
from google.auth import default
from prometheus_client import start_http_server
from helpers import invoke_servce

start_http_server(8080)
credentials, project_id = default()
subscription_id = os.getenv("SUBSCRIPTION_ID")
NUM_MESSAGES = int(os.getenv("BATCH_SIZE"))
LEASE_TIME = int(os.getenv("LEASE_TIME","15"))
SERVICE = os.getenv("SERVICE_URL")

# logger and subscriber

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)


# Callback function that processes incoming Pub/Sub messages
def callback(message: pubsub_v1.subscriber.message.Message):

    try:
        msg = message.data.decode('utf-8')
        json_data = json.loads(msg)
   

        no_of_retry = message.delivery_attempt
        print(f'No of Attempt : {no_of_retry}')
        print(f'Processing Message : {json_data}')
        response=invoke_servce(SERVICE,body=json_data)
        response.raise_for_status()
        
        message.ack()


    except Exception as e:
        print('error while processing message:', e)
        message.nack()  


if __name__ == "__main__":
    flow_control = FlowControl(
        max_bytes=104857600,
        max_messages=NUM_MESSAGES,
        max_lease_duration=30*LEASE_TIME
    )
    # Subscribe to the subscription and pass the callback
    future = subscriber.subscribe(subscription_path, callback=callback, flow_control=flow_control)

    # Keep the main thread alive while messages are being processed
    print(f"Listening for messages on {subscription_path}...")
    try:
        future.result()  # Blocks the main thread indefinitely, receiving messages
    except KeyboardInterrupt:
        future.cancel()  # Cancel the subscription when interrupted
        print("Subscription canceled.")
