resource "aws_s3_bucket" "this" {
  bucket = "bishop-industries-eu-west-2-sussexmews-website-files"
}

resource "aws_s3_bucket_public_access_block" "sussex-mews-bucket-public-enable" {
  bucket = aws_s3_bucket.this.id
  block_public_acls   = false
  block_public_policy = false
}

resource "aws_s3_bucket_policy" "allow_public_read_access" {
  bucket = aws_s3_bucket.this.id
  policy = data.aws_iam_policy_document.s3_public_access.json
}