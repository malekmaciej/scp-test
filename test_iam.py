import iam

account_id = "544974297782"
role_name = "test_role"
aws_policy_arn = "arn:aws:iam::aws:policy/ReadOnlyAccess"
role_arn = "arn:aws:iam::" + account_id + ":role/" + role_name
policy_name = "test_policy"
policy_document = "policy_document.json"
policy_arn = "arn:aws:iam::" + account_id + ":policy/" + policy_name

def get_policy_document_from_file(filename):
    with open(filename, "r") as f:
        return f.read()
    
# Tests

def test_create_role(session):
    iam.delete_role(session, role_name)
    assert iam.create_role(session, role_name) == role_arn

def test_delete_role(session):
    assert iam.delete_role(session, role_name) == 200

def test_create_role_with_tags_standard(session):
    iam.delete_role(session, role_name)
    assert iam.create_role_with_tags(session, role_name, "standard_tag_key", "standard_tag_value") == role_arn

def test_create_role_with_tags_protected(session):
    iam.delete_role(session, role_name)
    assert iam.create_role_with_tags(session, role_name, "GCSProtected", "GCSProtected_value") == role_arn

def test_attach_policy_unprotected_role(session):
    iam.create_role(session, role_name)
    assert iam.attach_role_policy(session, role_name, aws_policy_arn) == 200

def test_detach_policy(session):
    assert iam.dettach_role_policy(session, role_name, aws_policy_arn) == 200

def test_create_policy(session, policy_setup):
    iam.delete_policy(session, policy_arn)
    assert iam.create_policy(session, policy_name, get_policy_document_from_file(policy_document)) == policy_arn

def test_delete_policy(session):
    iam.create_policy(session, policy_name, get_policy_document_from_file(policy_document))
    assert iam.delete_policy(session, policy_arn) == 200

def test_create_policy_with_tags_standard(session, policy_setup):
    assert iam.create_policy_with_tags(session, policy_name, get_policy_document_from_file(policy_document), "standard_tag_key", "standard_tag_value") == policy_arn

def test_create_policy_with_tags_protected(session, policy_setup):
    assert iam.create_policy_with_tags(session, policy_name, get_policy_document_from_file(policy_document), "GCSProtected", "GCSProtected_value") == policy_arn
