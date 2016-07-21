from sense_hat import SenseHat
from datetime import datetime
from random import randrange, randint
from simple_salesforce import Salesforce

sense = SenseHat()
pi_names = ["CoolCat", "Black Box", "Speed Reader"]
locations = ["Car", "Home", "School"]
namerandint = randrange(1,3)
locationrandint = randrange(1,3)

now = datetime.now()
dt = datetime.now()
timenow = '%s:%s' % (now.hour,now.minute)

d = datetime.strptime(timenow, "%H:%M")
finaltime = d.strftime("%I:%M %p")

def write_sense_temp():
    sf = Salesforce(username='vsadmin2@gmail.com', password='ymHT3e3xMGyHMqo1', security_token='Sr99CXKsdY3ib90Vo0gdTe6T')
    print sf.Temperature__c.create({'Computer_Name__c':'CoolCat','Location__c':'Home','Temp__c':str(randint(70,99)), 'TimeOfReading__c':dt.isoformat("T")})
    


def get_sense_temp():
    sense_temp = sense.get_temperature()
    return sense_temp

print str(get_sense_temp()) + "," + '%s/%s/%s' % (now.month,now.day,now.year) + " " + finaltime + "," + pi_names[namerandint] +  "," + locations[locationrandint]

write_sense_temp()


    
