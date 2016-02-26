# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 15:21:36 2016

@author: DataLab1
"""

class SQSMessage():
    def __init__(self):
        self.messageAttributes = {
            'Author': {
            'StringValue': '',
            'DataType': 'String'
            },
            'Timestamp': {
            'StringValue': '',
            'DataType': 'String'
            },            
            'MessageType': {
            'StringValue': '',
            'DataType': 'String'   
            }
        }
        self.message = ''
    
    def SetAuthor(self,n):
        self.messageAttributes['Author']['StringValue'] = n

    def SetMessageType(self,n):
        self.messageAttributes['MessageType']['StringValue'] = n
        
    def SetTimestamp(self,n):
        self.messageAttributes['Timestamp']['StringValue'] = n
        
    def AttributeNames(self):
        return [i for i in self.messageAttributes.keys()]