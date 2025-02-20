import os

import aws_cdk as cdk

from provision.stacks import TraefikStack


app = cdk.App()
TraefikStack(app, "traefik")

app.synth()
