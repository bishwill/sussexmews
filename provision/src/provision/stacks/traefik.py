from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_iam as iam,
    aws_route53 as route53,
    Duration,
    Environment,
)
from constructs import Construct


class TraefikStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        dns_modifier_user = iam.User(
            self, id="dns-modifier-user", user_name="traefik-dns-modifier"
        )
        dns_modifier_user.apply_removal_policy(RemovalPolicy.DESTROY)

        dns_modifier_policy = iam.Policy(
            self,
            id="dns-modifier-policy",
            policy_name="DNSModifier",
            statements=[
                iam.PolicyStatement(
                    effect=iam.Effect.ALLOW,
                    actions=[
                        "route53:GetChange",
                        "route53:ChangeResourceRecordSets",
                        "route53:ListResourceRecordSets",
                    ],
                    resources=[
                        "arn:aws:route53:::hostedzone/*",
                        "arn:aws:route53:::change/*",
                    ],
                ),
                iam.PolicyStatement(
                    actions=["route53:ListHostedZonesByName"],
                    effect=iam.Effect.ALLOW,
                    resources=["*"],
                ),
            ],
        )
        dns_modifier_policy.attach_to_user(dns_modifier_user)

        hosted_zone = route53.HostedZone.from_lookup(
            self,
            id="hosted-zone",
            domain_name="sussexmews.co.uk",
        )

        route53.ARecord(
            self,
            "wildcard-record",
            zone=hosted_zone,
            record_name="*",
            ttl=Duration.seconds(300),
            target=route53.RecordTarget.from_ip_addresses("192.168.12.3"),
        )
