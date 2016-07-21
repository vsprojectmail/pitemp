from sense_hat import SenseHat
from datetime import datetime
from random import randrange

sense = SenseHat()
pi_names = ["CoolCat", "Black Box", "Speed Reader"]
locations = ["Car", "Home", "School"]
namerandint = randrange(1,3)
locationrandint = randrange(1,3)

now = datetime.now()
timenow = '%s:%s' % (now.hour,now.minute)

d = datetime.strptime(timenow, "%H:%M")
finaltime = d.strftime("%I:%M %p")





def get_sense_temp():
    sense_temp = sense.get_temperature()
    return sense_temp

print str(get_sense_temp()) + "," + '%s/%s/%s' % (now.month,now.day,now.year) + " " + finaltime + "," + pi_names[namerandint] +  "," + locations[locationrandint]




    
