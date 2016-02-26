# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:36:12 2016

@author: DataLab1
"""

import SQSManager as m

attributes = {'DelaySeconds': '5'}

#m.CreateQueue(m.queueName, attributes)

#m.PostMessage(m.queueName,"again, Thorneycreek","Ian")

m.ProcessMessages(m.queueName)