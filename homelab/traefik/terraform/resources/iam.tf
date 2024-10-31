resource "aws_iam_user" "traefik_dns_user" {
  name = "traefik-dns-modifier"
}

resource "aws_iam_user_policy" "traefik_dns_user_policy" {
  name = "DNSModifier"
  user = aws_iam_user.traefik_dns_user.name

  policy = jsonencode({
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "route53:GetChange",
        "route53:ChangeResourceRecordSets",
        "route53:ListResourceRecordSets"
      ],
      "Resource": [
        "arn:aws:route53:::hostedzone/*",
        "arn:aws:route53:::change/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": "route53:ListHostedZonesByName",
      "Resource": "*"
    }
  ]
})
}