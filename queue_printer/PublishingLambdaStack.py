from aws_cdk import (core, aws_lambda as _lambda, aws_sqs as sqs, aws_s3_assets as s3a)
from os import path

from .InboundQueueStack import InboundQueueStack


class PublishingLambdaStack(core.Stage):
    def __init__(self, scope: core.Construct, id: str, inbound_queue: sqs.Queue, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.function = _lambda.Function(self, "PublishingLambda",
                                         code=_lambda.Code.from_asset('queue_printer/publishing_lambda'),
                                         runtime=_lambda.Runtime.PYTHON_3_7,
                                         handler='main.handler',
                                         environment={
                                             "QUEUE_NAME": inbound_queue.queue_name
                                         }
                                         )
        inbound_queue.grant_send_messages(self.function)
