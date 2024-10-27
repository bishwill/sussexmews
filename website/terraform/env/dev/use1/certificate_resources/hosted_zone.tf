data "aws_route53_zone" "sussex_mews" {
  name         = "sussexmews.co.uk"
  private_zone = false
}