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
    
# Tests run as OrganizationAccountAccessRole

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
    assert iam.create_role_with_tags(session, role_name, "HSBC:AWS:GCS:Protection", "true") == role_arn

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
    assert iam.create_policy_with_tags(session, policy_name, get_policy_document_from_file(policy_document), "HSBC:AWS:GCS:Protection", "true") == policy_arn

## Administrator

# Creating role

def test_create_role_admin(session, session_admin):
    iam.delete_role(session, role_name)
    assert iam.create_role(session_admin, role_name) == role_arn

def test_delete_role_admin(session_admin):
    assert iam.delete_role(session_admin, role_name) == 200

def test_create_role_with_tags_standard_admin(session, session_admin):
    iam.delete_role(session, role_name)
    assert iam.create_role_with_tags(session_admin, role_name, "standard_tag_key", "standard_tag_value") == role_arn

def test_create_role_with_tags_protected_admin(session, session_admin):
    iam.delete_role(session, role_name)
    assert iam.create_role_with_tags(session_admin, role_name, "HSBC:AWS:GCS:Protection", "true") == "ERROR"

def test_delete_role_with_tags_admin(session, session_admin):
    iam.delete_role(session, role_name)
    iam.create_role_with_tags(session, role_name, "standard_tag_key", "standard_tag_value")
    assert iam.delete_role(session_admin, role_name) == 200

def test_delete_role_with_tags_protected_admin(session, session_admin):
    iam.delete_role(session, role_name)
    iam.create_role_with_tags(session, role_name, "HSBC:AWS:GCS:Protection", "true")
    assert iam.delete_role(session_admin, role_name) == "ERROR"

# Policy attaching/detaching

def test_attach_policy_unprotected_role_admin(session_admin):
    iam.create_role(session_admin, role_name)
    assert iam.attach_role_policy(session_admin, role_name, aws_policy_arn) == 200

def test_detach_policy_admin(session_admin):
    assert iam.dettach_role_policy(session_admin, role_name, aws_policy_arn) == 200

def test_create_policy_admin(session_admin, policy_setup):
    iam.delete_policy(session_admin, policy_arn)
    assert iam.create_policy(session_admin, policy_name, get_policy_document_from_file(policy_document)) == policy_arn

def test_delete_policy_admin(session_admin):
    iam.create_policy(session_admin, policy_name, get_policy_document_from_file(policy_document))
    assert iam.delete_policy(session_admin, policy_arn) == 200

def test_create_policy_with_tags_standard_admin(session_admin, policy_setup):
    assert iam.create_policy_with_tags(session_admin, policy_name, get_policy_document_from_file(policy_document), "standard_tag_key", "standard_tag_value") == policy_arn

def test_create_policy_with_tags_protected_admin(session_admin, policy_setup):
    error = "'An error occurred (AccessDenied) when calling the CreatePolicy operation: User: arn:aws:sts::" + account_id + ":assumed-role/Administrator/remote_session is not authorized to perform: iam:CreatePolicy on resource: policy test_policy with an explicit deny in a service control policy',)"
    assert iam.create_policy_with_tags(session_admin, policy_name, get_policy_document_from_file(policy_document), "HSBC:AWS:GCS:Protection", "true") == "ERROR"

# Tagging role

def test_tag_role_standard(session, session_admin, role_setup):
    assert iam.tag_role(session_admin, role_name, "standard_tag_key", "standard_tag_value") == 200

def untag_role_standard(session, session_admin, role_setup):
    assert iam.untag_role(session_admin, role_name, "standard_tag_key") == 200

def test_tag_role_protected(session, session_admin, role_setup):
    assert iam.tag_role(session_admin, role_name, "HSBC:AWS:GCS:Protection", "true") == "ERROR"

def untag_role_protected(session, session_admin, role_setup):
    iam.tag_role(session, role_name, "HSBC:AWS:GCS:Protection", "true")
    assert iam.untag_role(session_admin, role_name, "HSBC:AWS:GCS:Protection") == 200

