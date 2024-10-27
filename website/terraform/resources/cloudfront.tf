resource "aws_cloudfront_distribution" "s3_distribution" {
  origin {
    domain_name = aws_s3_bucket_website_configuration.this.website_endpoint
    origin_id   = aws_s3_bucket.this.bucket

    custom_origin_config {
        http_port = 80
        https_port = 443
        origin_protocol_policy = "http-only"
        origin_ssl_protocols   = ["TLSv1.2"]
    }
  }

  aliases = ["sussexmews.co.uk", "www.sussexmews.co.uk"]

  restrictions {
    geo_restriction {
      locations          = ["GB"]
      restriction_type = "whitelist"
    }
  }


  default_cache_behavior {
    allowed_methods  = ["GET", "HEAD"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = aws_s3_bucket.this.bucket

    forwarded_values {
      query_string = false

      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
    min_ttl     = 0
    default_ttl = 3600
    max_ttl     = 86400
  }

  viewer_certificate {
    acm_certificate_arn = data.aws_acm_certificate.sussexmews.arn
    ssl_support_method = "sni-only"
  }

  enabled = true
}


data "aws_acm_certificate" "sussexmews" {
  provider = aws.use1
  domain   = "*.sussexmews.co.uk"
  statuses = ["ISSUED"]
}