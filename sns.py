import boto3

def create_sns_topic(session, name, tags):
    sns_client = session.client('sns')
    try:
        response = sns_client.create_topic(
            Name=name,
            Tags=tags
        )
        return response['TopicArn']
    except Exception as e:
        return e

def delete_sns_topic(session,  topic_arn):
    sns_client = session.client('sns')
    try:
        response = sns_client.delete_topic(TopicArn=topic_arn)
        return response
    except Exception as e:
        return e
    
def tag_sns_topic(session, topic_arn, tags):
    sns_client = session.client('sns')
    try:
        response = sns_client.tag_resource(
            ResourceArn=topic_arn,
            Tags=tags
        )
        return response
    except Exception as e:
        return e
    
def delete_tag_sns_topic(session, topic_arn, tag_keys):
    sns_client = session.client('sns')
    try:
        response = sns_client.untag_resource(
            ResourceArn=topic_arn,
            TagKeys=tag_keys
        )
        return response
    except Exception as e:
        return e