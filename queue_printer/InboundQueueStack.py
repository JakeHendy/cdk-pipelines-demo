from aws_cdk import (core, aws_sqs as sqs)

class InboundQueueStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        self.queue = sqs.Queue(self, "InboundQueue", queue_name="InboundQueue")