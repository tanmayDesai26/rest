#!/usr/bin/env python3

import argparse
import os
import time
from pprint import pprint

import googleapiclient.discovery
import google.auth

credentials, project = google.auth.default()
service = googleapiclient.discovery.build('compute', 'v1', credentials=credentials)

zone = "us-west1-a"
firewallPort = 5000
firewallName = "allow-{}".format(firewallPort)
instanceName = "us"

print(project)
print(credentials)

# [START create_instance]
def create_instance(service, project, zone, instanceName):
    # Get the latest Debian Jessie image.
    image_response = service.images().getFromFamily(
        project="ubuntu-os-cloud", family="ubuntu-1804-lts").execute()
    source_disk_image = image_response['selfLink']

    # Configure the machine
    #change to f1-micro later
    machine_type = "zones/%s/machineTypes/e2-standard-2" % zone
    startup_script = open(
        os.path.join(
            os.path.dirname(__file__), 'startup-script.sh'), 'r').read()
    rest_server = open(
        os.path.join(
            os.path.dirname(__file__), 'rest-server.py'), 'r').read()
    rest_client = open(
        os.path.join(
            os.path.dirname(__file__), 'rest-client.py'), 'r').read()
    grpc_server = open(
        os.path.join(
            os.path.dirname(__file__), 'grpc-server.py'), 'r').read()
    grpc_client = open(
        os.path.join(
            os.path.dirname(__file__), 'grpc-client.py'), 'r').read()
    lab6_proto = open(
        os.path.join(
            os.path.dirname(__file__), 'lab6.proto'), 'r').read()
    flatirons_Winter_Sunrise_edit_2 = open(
        os.path.join(
            os.path.dirname(__file__), 'Flatirons_Winter_Sunrise_edit_2.jpg'), 'rb').read()

    config = {
        'name': instanceName,
        'machineType': machine_type,

        # Specify the boot disk and the image to use as a source.
        'disks': [
            {
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': source_disk_image,
                }
            }
        ],

        # Specify a network interface with NAT to access the public
        # internet.
        'networkInterfaces': [{
            'network': 'global/networks/default',
            'accessConfigs': [
                {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
            ]
        }],

        # Allow the instance to access cloud storage and logging.
        'serviceAccounts': [{
            'email': 'default',
            'scopes': [
                'https://www.googleapis.com/auth/devstorage.read_write',
                'https://www.googleapis.com/auth/logging.write'
            ]
        }],

        # Metadata is readable from the instance and allows you to
        # pass configuration from deployment scripts to instances.
        'metadata': {
            'items': [{
                # Startup script is automatically executed by the
                # instance upon startup.
                'key': 'startup-script',
                'value': startup_script
            },
            {
                'key': 'rest-client',
                'value': rest_client
            },
            {
                'key': 'rest-server',
                'value': rest_server
            },
            {
                'key': 'grpc-server',
                'value': grpc_server
            },
            {
                'key': 'grpc-client',
                'value': grpc_client
            },
            {
                'key': 'lab6-proto',
                'value': lab6_proto
            }]
        }
    }
    print(project)
    print(zone)

    return service.instances().insert(
        project=project,
        zone=zone,
        body=config).execute()
# [END create_instance]


# [START wait_for_operation]
def wait_for_operation(compute, project, zone, operation):
    print('Waiting for operation to finish...')
    while True:
        result = compute.zoneOperations().get(
            project=project,
            zone=zone,
            operation=operation).execute()

        if result['status'] == 'DONE':
            print("done.")
            if 'error' in result:
                raise Exception(result['error'])
            return result

        time.sleep(1)
# [END wait_for_operation]


# [START list_instances]
def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items'] if 'items' in result else None
# [END list_instances]

# [START create_firewall_rule]
def create_firewall_rule(service, project):
    firewall_body = {
        "name" : "allow-5000",
        "allowed": [
            {
            "IPProtocol": "tcp",
            "ports": [
                "5000"
            ]
            }
        ],
        "targetTags": [
            "allow-5000" 
        ],
        "sourceRanges": [
            "0.0.0.0/0"

        ]
    }
    service.firewalls().insert(project=project, body=firewall_body).execute()
# [END create_firewall_rule]


# [START set_network_tag_to_vm]
def set_network_tag_to_vm(service, project, zone, instanceName, fingerprint):
    tags_body ={
        'items':[
            "allow-5000"
        ],
        'fingerprint' : fingerprint
    }

    return service.instances().setTags(project=project, zone=zone, instance=instanceName, body=tags_body).execute()
# [END set_network_tag_to_vm]

operation = create_instance(service, project, zone, instanceName)
wait_for_operation(service, project, zone, operation['name'])
print("Your running instances are:")
#create_firewall_rule(service, project)
for instance in list_instances(service, project, zone):
    print(instance['name'])

try:
    instanceResp = service.instances().get(project=project, zone=zone,instance=instanceName).execute()
    # pylint: disable=maybe-no-member
    if instanceResp:
        instanceIP = instanceResp['networkInterfaces'][0]['accessConfigs'][0]['natIP']
        fingerprint = instanceResp['tags']['fingerprint']
        print(fingerprint)
        #set_network_tag_to_vm(service, project, zone, instanceName, fingerprint)
        print("Your blog is running at http://" + instanceIP + ":5000")
except googleapiclient.errors.HttpError as exp:
    print("Unable to lookup instance" + instanceName + "for IP address")
    print(exp)
        