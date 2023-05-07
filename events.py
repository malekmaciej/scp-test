import boto3

def create_event_rule(session, rule_name, schedule_expression, tags):
    client = session.client('events')
    try:
        response = client.put_rule(
            Name=rule_name,
            ScheduleExpression=schedule_expression,
            State='ENABLED',
            Tags=tags
        )
        return response
    except Exception as e:
        return e
    
def delete_event_rule(session, rule_name):
    client = session.client('events')
    try:
        response = client.delete_rule(
            Name=rule_name
        )
        return response
    except Exception as e:
        return e
    
def create_tag_event_rule(session, rule_name, tags):
    client = session.client('events')
    try:
        response = client.tag_resource(
            ResourceArn=rule_name,
            Tags=tags
        )
        return response
    except Exception as e:
        return e
    
def delete_tag_event_rule(session, rule_name, tag_keys):
    client = session.client('events')
    try:
        response = client.untag_resource(
            ResourceArn=rule_name,
            TagKeys=tag_keys
        )
        return response
    except Exception as e:
        return e

def enable_rule(session, rule_name):
    client = session.client('events')
    try:
        response = client.enable_rule(
            Name=rule_name
        )
        return response
    except Exception as e:
        return e
    
def disable_rule(session, rule_name):
    client = session.client('events')
    try:
        response = client.disable_rule(
            Name=rule_name
        )
        return response
    except Exception as e:
        return e