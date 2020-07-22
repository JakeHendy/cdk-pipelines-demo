from aws_cdk import (core, aws_lambda as _lambda, aws_sqs as sqs, aws_s3_assets as s3a)
from os import path

from .InboundQueueStack import InboundQueueStack


class PublishingLambdaStack(core.Stage):
    def __init__(self, scope: core.Construct, id: str, inbound_queue: sqs.Queue, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.function = _lambda.Function(self, "PublishingLambda",
                                         code=_lambda.Code.from_inline(
                                             """
import sys
import os
import boto3
from typing import Dict
QUEUE_NAME = os.environ.get("QUEUE_NAME", "jh-publishing-queue")

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName=QUEUE_NAME)

def handler(event: Dict[str, str], context: Dict[str, str]) -> Dict[str, str]:
    print("Lambda running")
    has_key = "number_of_messages" in event
    number_of_messages = event["number_of_messages"] if has_key else 10

    for i in range(0, number_of_messages):
        print(f"====== Sending message {i} ======")
        response = queue.send_message(MessageBody=f"This is message number {i}")
        print(response.get('MessageId'))
        print(response.get('MD5OfMessageBody'))

                                             """
                                         ),
                                         runtime=_lambda.Runtime.PYTHON_3_7,
                                         handler='index.handler',
                                         environment={
                                             "QUEUE_NAME": inbound_queue.queue_name
                                         }
                                         )
        inbound_queue.grant_send_messages(self.function)
