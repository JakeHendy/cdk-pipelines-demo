from aws_cdk import (core, pipelines)
from .InboundQueueStack import InboundQueueStack
from .PublishingLambdaStack import PublishingLambdaStack

class QueuePrinter(core.Stage):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        QueuePrinterStack(self, "QueuePrinterStack")


class QueuePrinterStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        self.queue_stack = InboundQueueStack(self, "InboundQueue")
        self.publishing_lambda = PublishingLambdaStack(self, "PublishingLambda", self.queue_stack.queue)