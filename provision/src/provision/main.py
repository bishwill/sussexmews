import os

import aws_cdk as cdk
from aws_cdk import Tags, Environment

from provision.stacks import TraefikStack


def main() -> None:
    app = cdk.App()
    traefik_stack = TraefikStack(
        app, "traefik", env=Environment(account="499844099075", region="eu-west-2")
    )
    Tags.of(traefik_stack).add("stack", "traefik")
    app.synth()
