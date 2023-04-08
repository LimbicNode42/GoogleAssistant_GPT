import boto3

def get_org_key():
    ssm_client = boto3.client('ssm')
    org_key_name = 'OPENAI_ORG_KEY'
    org_key_value = ssm_client.get_parameter(Name=org_key_name, WithDecryption=True)['Parameter']['Value']
    # print(org_key_value)
    return org_key_value
    
def get_api_key():
    ssm_client = boto3.client('ssm')
    api_key_name = 'OPENAI_API_KEY'
    api_key_value = ssm_client.get_parameter(Name=api_key_name, WithDecryption=True)['Parameter']['Value']
    # print(api_key_value)
    return api_key_value