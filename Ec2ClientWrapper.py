# -*- coding: utf-8 -*-

import os, sys, re, csv, requests, datetime, traceback, time
from pprint import pprint
import json
import boto3


class Ec2ClientWrapper(object):

    """
        Initialize.
    """
    def __init__(self):
        self.ec2 = boto3.resource('ec2')


    """
        Stop instance.
    """
    def start(self, instanceId):
        ids = [instanceId]
        self.ec2.instances.filter(InstanceIds=ids).start()


    """
        Stop instance.
    """
    def stop(self, instanceId):
        ids = [instanceId]
        self.ec2.instances.filter(InstanceIds=ids).stop()


    """
        Terminate instance.
    """
    def terminate(self, instanceId):
        ids = [instanceId]
        self.ec2.instances.filter(InstanceIds=ids).terminate()


    """
        Create instance.
        return: Created instance.
    """
    def create(self, amiId, keyName, securityGroupId):
        # Setting of EBS.(Delete volume when related instance has been terminated.)
        blockDeviceMappings = [{
            "DeviceName": "/dev/sda1",
            "Ebs": {
                "DeleteOnTermination": True,
                "VolumeType": "gp2"
            },
        }]

        ret = self.ec2.create_instances(
                                        ImageId=amiId,
                                        MinCount=1,
                                        MaxCount=1,
                                        InstanceType="t2.micro",
                                        KeyName=keyName,
                                        SecurityGroupIds=[securityGroupId],
                                        BlockDeviceMappings=blockDeviceMappings
                                        )
        # Waiting for been running to acquire public_ip.
        createdInstanceId = ret[0].instance_id
        ret[0].wait_until_running()
        createdInstance = self.getInstanceById(createdInstanceId)
        return createdInstance


    """
        Get instance by instanceId.
    """
    def getInstanceById(self, instanceId):
        return self.ec2.Instance(instanceId)
