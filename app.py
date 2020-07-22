#!/usr/bin/env python3

from aws_cdk import core

from cdk_pipeline_demo_stack import CdkPipelineDemoStack
from queue_printer import QueuePrinterStage
app = core.App()

CdkPipelineDemoStack(app, "cdk-pipeline-demo", 
QueuePrinterStage.QueuePrinter(app, "queueprinter")
                    ,
                    QueuePrinterStage.QueuePrinter(app, "queueprinterue1", env = { "account": "649766597883", "region": "us-east-1" }))

app.synth()
