# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 15:54:30 2016

@author: DataLab1

Provides encryption / decryption helper functions
"""
import simplecrypt

secret = 'Shbu4@c0h'

def encrypt(m):
    s = simplecrypt.encrypt(secret, m.message)
    m.SetVersion(s[0:4])
    m.message = s[4:].encode('utf-16')
    return m
    
def decrypt(m):
    src = m.EncryptedMessage()
    return simplecrypt.decrypt(secret,src)