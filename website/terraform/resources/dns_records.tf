resource "aws_route53_record" "cloudfront" {
  zone_id = aws_route53_zone.sussex_mews.zone_id
  name    = ""
  type    = "A"

alias {
    name                   = aws_cloudfront_distribution.s3_distribution.domain_name
    zone_id                = aws_cloudfront_distribution.s3_distribution.hosted_zone_id
    evaluate_target_health = true
  }
}

resource "aws_route53_record" "www" {
  zone_id = aws_route53_zone.sussex_mews.zone_id
  name    = "www"
  type    = "CNAME"
  ttl     = 300
  records = ["sussexmews.co.uk"]
}

