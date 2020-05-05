#!/usr/bin/env python

import boto3
import time
from utils.json_writer import json_writer
from utils.connection import connect_aws_service

#Delete all the DNS records used to the green Env.
def get_ips(regions):
    for region in regions:
        client = connect_aws_service(region, 'ec2')

        PublicInfo = list()
        response = client.describe_network_interfaces(
            Filters=[
                {
                    'Name': 'attachment.status',
                    'Values': ['attached']
                },
            ],
        )

        for NetworkInterfaces in response:
            NetworkInterfaces = response.get('NetworkInterfaces')
            for details in NetworkInterfaces:
                try:  
                    PublicInfo.append(details.get('Association').get('PublicIp'))
                except:
                    pass

        json_writer('output/' + region + '-info.json', PublicInfo)