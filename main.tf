module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = "wp-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["us-east-1a", "us-east-1b", "us-east-1c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102te.0/24", "10.0.103.0/24"]

  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}

output "metavpc" { value = module.vpc }

module "eks" {

  source             = "./eks"
  public_eks_subnets = module.vpc.metavpc.public_subnets
  vpc_id             = module.vpc.metavpc.metavpc.vpc_id

}

terraform {
  backend "s3" {
    bucket = "tf-state-for-si3mshady"
    key    = "tfstate"
    region = "us-east-1"
  }
}
