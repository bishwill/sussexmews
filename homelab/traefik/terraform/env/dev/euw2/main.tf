terraform {
  required_version = ">= 0.13"

  backend "s3" {

    bucket = "bishop-industries-terraform-state"
    key    = "sussex-mews-traefik-https.tfstate"
    region = "eu-west-1"
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~>5.0"
    }
  }

}

provider "aws" {
  alias  = "application"
  region = "eu-west-2"
}

resource "aws_servicecatalogappregistry_application" "sussex_mews" {
  provider    = aws.application
  name        = "SussexMewsTraefik"
  description = "Sussex Mews Traefik Resources"
}


provider "aws" {
  region = "eu-west-2"
  default_tags {
    tags = aws_servicecatalogappregistry_application.sussex_mews.application_tag
  }
}


module "resources" {
  source = "../../../resources"
}
