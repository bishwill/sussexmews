data "aws_iam_policy_document" "s3_public_access" {
  version = "2012-10-17"
  statement {
    sid = "S3PublicReadAccess"
    effect = "Allow"
    principals {
      identifiers = ["*"]
      type = "*"
    }
    actions = [
      "s3:GetObject",
    ]
    resources = [
      "arn:aws:s3:::${aws_s3_bucket.this.bucket}/*",
    ]
  }
}
