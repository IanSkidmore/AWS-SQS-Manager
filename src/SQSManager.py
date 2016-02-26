# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:07:12 2016

@author: DataLab1

Helper routines to manage AWS SQS resources
"""

import boto3
queueName = "ThorneycreekSQS"

def CreateQueue(queueName,attributes):
    sqs = boto3.resource('sqs')
            
    queue = sqs.create_queue(QueueName=queueName,Attributes=attributes)
    
    print queue.url
    
def PostMessage(queueName,messageText,author):
    sqs = boto3.resource('sqs')
    attributes = {'Author': {
        'StringValue': author,
        'DataType': 'String'
        }
    }
    queue = sqs.get_queue_by_name(QueueName=queueName)
    response = queue.send_message(MessageBody=messageText, MessageAttributes=attributes)

    print response.get('MessageId')

def ProcessMessages(queueName):
    sqs = boto3.resource('sqs')
    
    queue = sqs.get_queue_by_name(QueueName=queueName)
    
    for message in queue.receive_messages(MessageAttributeNames=['Author']):

        if message.message_attributes is not None:
            authorName = message.message_attributes.get('Author').get('StringValue')
            if authorName:
                print "Hello, {0}! from {1}".format(message.body,authorName)
            else:
               print "Hello, {0}!".format(message.body)
                 
    message.delete()

