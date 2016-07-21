from sense_hat import SenseHat
from datetime import datetime
from random import randrange, randint
from simple_salesforce import Salesforce

sense = SenseHat()
dt = datetime.now()

def write_sense_temp():
    sf = Salesforce(username='vsadmin2@gmail.com', password='ymHT3e3xMGyHMqo1', security_token='Sr99CXKsdY3ib90Vo0gdTe6T')
    return sf.Temperature__c.create({'Computer_Name__c':'CoolCat','Location__c':'Home','Temp__c':str(get_sense_temp()), 'TimeOfReading__c':dt.isoformat("T")})
    


def get_sense_temp():
    sense_temp = sense.get_temperature()
    return sense_temp


print write_sense_temp()


    
