import boto3


def create_role(session, role_name) -> str:
    iam = session.client('iam')
    try:
        response = iam.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=open('trust_policy.json').read()
        )
        return response["Role"]["Arn"]
    except Exception as e:
        return "ERROR"


def create_role_with_tags(session, role_name, key, value) -> str:
    iam = session.client('iam')
    try:
        response = iam.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=open('trust_policy.json').read(),
            Tags=[
                {
                    'Key': key,
                    'Value': value
                },
            ]
        )
        return response['Role']['Arn']
    except Exception as e:
        return "ERROR"


def tag_role(session, role_name, key, value) -> int:
    iam = session.client('iam')
    try:
        response = iam.tag_role(
            RoleName=role_name,
            Tags=[
                {
                    'Key': key,
                    'Value': value
                },
            ]
        )
        return response["ResponseMetadata"]["HTTPStatusCode"]
    except Exception as e:
        return "ERROR"


def delete_role(session, role_name) -> int:
    iam = session.client('iam')
    try:
        response = iam.delete_role(
            RoleName=role_name
        )
        return response["ResponseMetadata"]["HTTPStatusCode"]
    except Exception as e:
        return "ERROR"


def untag_role(session, role_name, key):
    iam = session.client('iam')
    try:
        response = iam.untag_role(
            RoleName=role_name,
            TagKeys=[
                key,
            ]
        )
        return response["ResponseMetadata"]["HTTPStatusCode"]
    except Exception as e:
        return "ERROR"


def attach_role_policy(session, role_name, policy_arn) -> int:
    iam = session.client('iam')
    try:
        response = iam.attach_role_policy(
            RoleName=role_name,
            PolicyArn=policy_arn
        )
        return response["ResponseMetadata"]["HTTPStatusCode"]
    except Exception as e:
        return "ERROR"


def dettach_role_policy(session, role_name, policy_arn) -> None:
    iam = session.client('iam')
    try:
        response = iam.detach_role_policy(
            RoleName=role_name,
            PolicyArn=policy_arn
        )
        return response["ResponseMetadata"]["HTTPStatusCode"]
    except Exception as e:
        return "ERROR"


def create_policy(session, policy_name, policy_document):
    iam = session.client('iam')
    try:
        response = iam.create_policy(
            PolicyName=policy_name,
            PolicyDocument=policy_document
        )
        return response["Policy"]["Arn"]
    except Exception as e:
        return "ERROR"


def create_policy_with_tags(session, policy_name, policy_document, key, value):
    iam = session.client('iam')
    try:
        response = iam.create_policy(
            PolicyName=policy_name,
            PolicyDocument=policy_document,
            Tags=[
                {
                    'Key': key,
                    'Value': value
                },
            ]
        )
        return response["Policy"]["Arn"]
    except Exception as e:
        return "ERROR"


def delete_policy(session, policy_name):
    iam = session.client('iam')
    try:
        response = iam.delete_policy(
            PolicyArn=policy_name
        )
        return response["ResponseMetadata"]["HTTPStatusCode"]
    except Exception as e:
        return "ERROR"


def tag_policy(session, policy_name, key, value):
    iam = session.client('iam')
    try:
        response = iam.tag_policy(
            PolicyArn=policy_name,
            Tags=[
                {
                    'Key': key,
                    'Value': value
                },
            ]
        )
        return response["ResponseMetadata"]["HTTPStatusCode"]
    except Exception as e:
        return "ERROR"


def untag_policy(session, policy_name, key):
    iam = session.client('iam')
    try:
        response = iam.untag_policy(
            PolicyArn=policy_name,
            TagKeys=[
                key,
            ]
        )
        return response["ResponseMetadata"]["HTTPStatusCode"]
    except Exception as e:
        return "ERROR"