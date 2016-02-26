# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:07:12 2016

@author: DataLab1

Helper routines to manage AWS SQS resources
"""

import boto3

class SQSManager():
    
    def __init__(self, name, attributes):
        self.queueName = name
        self.sqs = boto3.resource('sqs')
        self.attributes = attributes

    def CreateQueue(self):           
        queue = self.sqs.create_queue(QueueName=self.queueName,Attributes=self.attributes)        
        return queue
        
    def FetchQueue(self):
        try:
            queue = self.sqs.get_queue_by_name(QueueName=self.queueName)
        except:
            queue = self.CreateQueue()
        return queue
        
    def PostMessage(self,m):
        import datetime
        queue = self.FetchQueue()
        m.SetTimestamp(datetime.datetime.now().isoformat())
        response = queue.send_message(MessageBody=m.message, MessageAttributes=m.messageAttributes)
        return response.get('MessageId')
    
    def ProcessMessages(self, attributeNames):  
        queue = self.FetchQueue()
        return queue.receive_messages(MessageAttributeNames=attributeNames)
