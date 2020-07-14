#!/usr/bin/env python3

from aws_cdk import core

from cdk_pipeline_demo.cdk_pipeline_demo_stack import CdkPipelineDemoStack


app = core.App()
CdkPipelineDemoStack(app, "cdk-pipeline-demo")

app.synth()
