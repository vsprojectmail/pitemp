from simple_salesforce import Salesforce
from datetime import datetime
dt = datetime.now()
from random  import  randint
sf = Salesforce(username='vshighadmin@gmail.com', password='qwertyu1love', security_token='mQOWJP4u9dTAt2vi0HdNiNeS3')
print sf.Temperature__c.create({'Computer_Name__c':'CoolCat','Location__c':'Home','Temp__c':str(randint(70,99)), 'TimeOfReading__c':dt.isoformat("T")})
