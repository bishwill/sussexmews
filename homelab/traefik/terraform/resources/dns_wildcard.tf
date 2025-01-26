data "aws_route53_zone" "sussex_mews" {
    name = "sussexmews.co.uk"
}

resource "aws_route53_record" "wildcard" {
  zone_id = data.aws_route53_zone.sussex_mews.zone_id
  name    = "*"
  type    = "A"
  ttl     = 300
  records = ["192.168.12.3"]
}