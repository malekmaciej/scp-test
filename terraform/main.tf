# "aws:PrincipalArn": "arn:aws:iam::349438938377:role/ADFS-InfraDevOps"

resource "aws_organizations_policy" "GCSProtectedResources" {
  name        = "GCS-Protected-Resources"
  description = "Policy to protect GCS resources deployed to Project Accounts"
  type        = "SERVICE_CONTROL_POLICY"
  content     = data.aws_iam_policy_document.GCSProtectedResources.json
  tags = {
    terraform = true
  }
}

resource "aws_organizations_policy_attachment" "attach_protected_scp_1" {
  policy_id = aws_organizations_policy.GCSProtectedResources.id
  target_id = "544974297782"
}