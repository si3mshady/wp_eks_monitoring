terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
   
    }
  }

  required_version = ">=0.14.9"

}


provider "aws" {
  version = "~>3.0"
  region  = "us-east-1"
}