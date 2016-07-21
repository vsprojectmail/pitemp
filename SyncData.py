from simple_salesforce import Salesforce
from datetime import date

sf = Salesforce(username='vsadmin2@gmail.com', password='ymHT3e3xMGyHMqo1', security_token='Sr99CXKsdY3ib90Vo0gdTe6TOjM9vAiX7nyzxUex9Hw2DLAoC')
print 'Login Successful'
print sf
'''
out = sf.Contact.create({'LastName':'Memon','Email':'abc123@example.com'})
print out

abc = sf.Contact.get ('0033600000LIv4jAAD')
print abc
'''
sf.query("CREATE DATABASE db123")
sf.query("USE db123")
print sf
