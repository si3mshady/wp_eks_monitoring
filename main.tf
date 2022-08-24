module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = "wp-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["us-east-1a", "us-east-1b", "us-east-1c"]

  public_subnets  = [for i in range(5, 255, 2) : cidrsubnet(var.vpc_cidr, 10, i)]

  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}

module "eks" {

  source             = "./eks"
  public_eks_subnets = [for cidr in module.vpc.public_subnets_cidr_blocks: cidr.public_subnets_cidr_blocks ]
  vpc_id             = module.vpc.vpc_id

}

terraform {
  backend "s3" {
    bucket = "tf-state-for-si3mshady"
    key    = "tfstate"
    region = "us-east-1"
  }
}
