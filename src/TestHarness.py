# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:36:12 2016

@author: DataLab1
"""

import SQSManager as mgr
import SQSMessage as m

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

q = mgr.SQSManager("ThorneycreekSQS",queueAttributes)


msg = m.SQSMessage()
'''
print msg.messageAttributes
print msg.AttributeNames()

msg.SetAuthor('Ian')
msg.SetMessageType('New Class Message')
print msg.messageAttributes

msg.message = ", Thorneycreek"
print q.PostMessage(msg)
msg.message = "again, Thorneycreek"
print q.PostMessage(msg)
msg.message = "once more, Thorneycreek"
print q.PostMessage(msg)
msg.message = "a fourth time, Thorneycreek"
print q.PostMessage(msg)
msg.message = "for the last time, Thorneycreek"
print q.PostMessage(msg)


'''
messages = q.ProcessMessages(msg.AttributeNames())
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
        
    messages = q.ProcessMessages(msg.AttributeNames())
