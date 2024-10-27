terraform {
  required_version = ">= 0.13"

  backend "s3" {

    bucket = "bishop-industries-terraform-state"
    key    = "sussex-mews-website.tfstate"
    region = "eu-west-1"
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~>5.0"
    }
  }

}

# Create application using aliased 'application' provider
provider "aws" {
  alias  = "application"
  region = local.aws_region
}

resource "aws_servicecatalogappregistry_application" "sussex_mews" {
  provider    = aws.application
  name        = "SussexMewsWebsite"
  description = "sussexmews.com Website"
}


provider "aws" {
  region = local.aws_region
  default_tags {
    tags = aws_servicecatalogappregistry_application.sussex_mews.application_tag
  }
}

provider "aws" {
  alias = "use1"
  region = "us-east-1"
  default_tags {
    tags = aws_servicecatalogappregistry_application.sussex_mews.application_tag
  }
}

module "resources" {
  source = "../../../resources"
  providers = {
    aws.use1 = aws.use1
  }
}
