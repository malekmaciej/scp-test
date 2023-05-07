import boto3

def attach_service_control_policy(policy_id, account_id):
    org = boto3.client('organizations')
    try:
        response = org.attach_policy(
                PolicyId=policy_id,
                TargetId=account_id
        )
        print(response)
    except Exception as e:
        print(e)


def dettach_service_control_policy(policy_id, account_id):
    org = boto3.client('organizations')
    try:
        response = org.detach_policy(
                PolicyId=policy_id,
                TargetId=account_id
        )
        print(response)
    except Exception as e:
        print(e)