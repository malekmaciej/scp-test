import boto3

def create_ssm_parameter(session, name, value, tags):
    ssm = session.client('ssm')
    try:
        response = ssm.put_parameter(
            Name=name,
            Value=value,
            Type='String',
            Overwrite=True,
            Tags=tags
        )
        return response['Tier']
    except Exception as e:
        return e

def delete_ssm_parameter(session, name):
    ssm = session.client('ssm')
    try:
        response = ssm.delete_parameter(
        Name=name
        )
        return response
    except Exception as e:
        return e

def create_tag_ssm_parameter(session, name, tags):
    ssm = session.client('ssm')
    try:
        response = ssm.add_tags_to_resource(
            ResourceType='Parameter',
            ResourceId=name,
            Tags=tags
            )
        return response
    except Exception as e:
        return e

def delete_tag_ssm_parameter(session, name, tagkeys):
    ssm = session.client('ssm')
    try:
        response = ssm.remove_tags_from_resource(
            ResourceType='Parameter',
            ResourceId=name,
            TagKeys=tagkeys
            )
        return response
    except Exception as e:
        return e