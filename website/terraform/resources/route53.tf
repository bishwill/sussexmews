resource "aws_route53domains_registered_domain" "sussex_mews" {
  domain_name = "sussexmews.co.uk"

  name_server {
    name = "ns-1767.awsdns-28.co.uk"
  }

  name_server {
    name = "ns-1078.awsdns-06.org"
  }


  name_server {
    name = "ns-956.awsdns-55.net"
  }

  name_server {
    name = "ns-288.awsdns-36.com"
  }

}

resource "aws_route53_zone" "sussex_mews" {
  name = "sussexmews.co.uk"
  comment = "sussexmews.co.uk Hosted Zone"
}