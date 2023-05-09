data "aws_iam_policy_document" "GCSProtectedResources" {
  statement {
    sid    = "ProtectGCSResources"
    effect = "Deny"
    actions = [
      "iam:Update*",
      "iam:Put*",
      "iam:Detach*",
      "iam:Delete*",
      "iam:Create*",
      "iam:Attach*",
      "iam:Remove*",
      "iam:Untag*",
      "iam:Tag*",
      "ssm:PutParameter",
      "ssm:DeleteParameters",
      "ssm:DeleteParameter",
      "ssm:AddTagsToResource",
      "events:Remove*",
      "events:Put*",
      "events:EnableRule",
      "events:DisableRule",
      "events:Delete*",
      "events:TagResource",
      "sns:DeleteTopic",
      "sns:TagResource",
      "sns:UntagResource"
    ]
    resources = ["*"]
    condition {
      test     = "StringNotLike"
      variable = "aws:PrincipalArn"
      values   = ["arn:aws:iam::*:role/OrganizationAccountAccessRole"]
    }

    condition {
      test     = "StringEqualsIgnoreCase"
      variable = "aws:RequestTag/HSBC:AWS:GCS:Protection"
      values   = [var.protected]
    }
  }



  statement {
    sid    = "ProtectGCSTag"
    effect = "Deny"
    actions = [
      "iam:Update*",
      "iam:Put*",
      "iam:Detach*",
      "iam:Delete*",
      "iam:Create*",
      "iam:Attach*",
      "iam:Remove*",
      "iam:Untag*",
      "iam:Tag*",
      "ssm:PutParameter",
      "ssm:DeleteParameters",
      "ssm:DeleteParameter",
      "ssm:AddTagsToResource",
      "events:Remove*",
      "events:Put*",
      "events:EnableRule",
      "events:DisableRule",
      "events:Delete*",
      "events:TagResource",
      "sns:DeleteTopic",
      "sns:TagResource",
      "sns:UntagResource"
    ]

    resources = ["*"]

    condition {
      test     = "StringNotLike"
      variable = "aws:PrincipalArn"
      values   = ["arn:aws:iam::*:role/OrganizationAccountAccessRole"]
    }

    condition {
      test     = "StringEqualsIgnoreCase"
      variable = "aws:RequestTag/HSBC:AWS:GCS:Protection"
      values   = [var.protected]
    }
  }
}
