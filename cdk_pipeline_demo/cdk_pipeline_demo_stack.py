from aws_cdk import (core,
                     aws_codepipeline,
                     aws_codepipeline_actions,
                     pipelines
                     )


class CdkPipelineDemoStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, the_application: core.Stage, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        source_artifact = aws_codepipeline.Artifact()
        cloud_artifact = aws_codepipeline.Artifact()

        source_action = aws_codepipeline_actions.GitHubSourceAction(

            oauth_token=core.SecretValue.secrets_manager("github-token"),
            output=source_artifact,
            action_name="GitHub",
            owner="JakeHendy",
            repo="cdk-pipelines-demo",
            trigger=aws_codepipeline_actions.GitHubTrigger.WEBHOOK
        )

        
        synth_action = pipelines.SimpleSynthAction(
            install_command="pip install -r requirements.txt",
            synth_command="npx cdk synth",
            source_artifact=source_artifact,
            cloud_assembly_artifact=cloud_artifact
        ) 
        pipeline = pipelines.CdkPipeline(self, "Pipeline",
        
                                         cloud_assembly_artifact=cloud_artifact,
                                         source_action=source_action,
                                         synth_action=synth_action)
        # The code that defines your stack goes here

        pipeline.add_application_stage(the_application)
