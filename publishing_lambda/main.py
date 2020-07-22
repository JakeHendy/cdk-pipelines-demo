import sys
import os
import boto3
from typing import Dict
QUEUE_NAME = os.environ.get("QUEUE_NAME", "jh-publishing-queue")

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName=QUEUE_NAME)

def handler(event: Dict[str, str], context: Dict[str, str]) -> Dict[str, str]:
    print("Lambda running")
    has_key = "number_of_messages" in event.keys
    number_of_messages = event["number_of_messages"] if has_key else 10

    for i in range(0, number_of_messages):
        print(f"====== Sending message {i} ======")
        response = queue.send_message(MessageBody=f"This is message number {i}")
        print(response.get('MessageId'))
        print(response.get('MD5OfMessageBody'))

