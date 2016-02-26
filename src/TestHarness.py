# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:36:12 2016

@author: DataLab1
"""

import SQSManager as m

queueAttributes = {'DelaySeconds': '5', 'ReceiveMessageWaitTimeSeconds': '1'}
messageAttributes = {'Author': {
        'StringValue': 'Ian',
        'DataType': 'String'
        },
        'MessageType': {
        'StringValue': 'TestMessage',
        'DataType': 'String'   
        }
}

q = m.SQSManager("ThorneycreekSQS",queueAttributes)
'''
print q.PostMessage(", Thorneycreek",messageAttributes)
print q.PostMessage("again, Thorneycreek",messageAttributes)
print q.PostMessage("once more, Thorneycreek",messageAttributes)
print q.PostMessage("a fourth time, Thorneycreek",messageAttributes)
print q.PostMessage("for the last time, Thorneycreek",messageAttributes)

'''
messages = q.ProcessMessages(['Author','MessageType'])
while len(messages) > 0:

    for message in messages:
        if message.message_attributes is not None:
            authorName = message.message_attributes.get('Author').get('StringValue')
    
            msgType = message.message_attributes.get('MessageType').get('StringValue')
            print "This is a message of type {0}".format(msgType)
    
            if authorName:
                print "Hello {0} from {1}".format(message.body,authorName)
            else:
               print "Hello {0}!".format(message.body)
                     
        message.delete()
        
    print 'polling for more messages'
    messages = q.ProcessMessages(['Author','MessageType'])
