import boto3
from utils.connection import connect_aws_service

def get_all_regions():
    # List all regions
    client = boto3.client('ec2')
    regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
    return regions