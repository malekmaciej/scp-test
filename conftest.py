import boto3
import iam
import pytest

account_id = "544974297782"
role_name = "test_role"
policy_name = "test_policy"
policy_arn = "arn:aws:iam::" + account_id + ":policy/" + policy_name

profile_name = "priv"
remote_account_role_arn = "arn:aws:iam::544974297782:role/OrganizationAccountAccessRole"
remote_admin_account_role_arn = "arn:aws:iam::544974297782:role/Administrator"
    

@pytest.fixture(scope="function")
def session():
    session = boto3.Session(profile_name=profile_name)
    sts = session.client("sts")
    response = sts.assume_role(
        RoleArn=remote_account_role_arn,
        RoleSessionName="remote_session"
    )
    new_session = boto3.Session(aws_access_key_id=response['Credentials']['AccessKeyId'],
                      aws_secret_access_key=response['Credentials']['SecretAccessKey'],
                      aws_session_token=response['Credentials']['SessionToken'])
    return new_session

@pytest.fixture(scope="function")
def session_admin():
    session = boto3.Session(profile_name=profile_name)
    sts = session.client("sts")
    response = sts.assume_role(
        RoleArn=remote_admin_account_role_arn,
        RoleSessionName="remote_session"
    )
    new_session = boto3.Session(aws_access_key_id=response['Credentials']['AccessKeyId'],
                      aws_secret_access_key=response['Credentials']['SecretAccessKey'],
                      aws_session_token=response['Credentials']['SessionToken'])
    return new_session

@pytest.fixture(scope="function")
def policy_setup(request, session):
    print("\nDoing setup - creating IAM Role and Policy")
    iam.delete_policy(session, policy_arn)
    iam.create_role(session, role_name)
    def fin():
        print("\nDoing IAM Role/Policy teardown")
        iam.delete_role(session, role_name)
        iam.delete_policy(session, policy_arn)
    request.addfinalizer(fin)

@pytest.fixture(scope="function")
def role_setup(request, session):
    print("\nDoing IAM Role setup")
    iam.create_role(session, role_name)
    def fin():
        print("\nDoing IAM Role teardown")
        iam.delete_role(session, role_name)
    request.addfinalizer(fin)

@pytest.fixture(scope="module")
def set_connection():
    boto3.setup_default_session(profile_name=profile_name)

