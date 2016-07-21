from simple_salesforce import Salesforce
from datetime import datetime
dt = datetime.now()
from random  import  randint
sf = Salesforce(username='vsadmin2@gmail.com', password='ymHT3e3xMGyHMqo1', security_token='Sr99CXKsdY3ib90Vo0gdTe6T')
print sf.Temperature__c.create({'Computer_Name__c':'CoolCat','Location__c':'Home','Temp__c':str(randint(70,99)), 'TimeOfReading__c':dt.isoformat("T")})
