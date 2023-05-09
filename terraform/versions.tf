terraform {
  required_version = "~>1.3.9"
}

provider "aws" {
  region  = "eu-central-1"
  profile = "priv"
}