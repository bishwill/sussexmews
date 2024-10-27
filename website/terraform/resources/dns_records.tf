resource "aws_route53_record" "www" {
  zone_id = aws_route53_zone.sussex_mews.zone_id
  name    = "www"
  type    = "CNAME"
  ttl     = 300
  records = ["sussexmews.co.uk"]
}