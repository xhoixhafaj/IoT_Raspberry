import pyrebase
import urllib
from klasatP import KrijoModulet
from  dht11example import Sensori
import time


firebaseConfig ={
    'apiKey': "AIzaSyDCUmoRDgWL_pz_jpBh16B0b2RlWMYv5j0",
    'authDomain': "iotrpi-39b89.firebaseapp.com",
    'databaseURL': "https://iotrpi-39b89-default-rtdb.firebaseio.com",
    'projectId': "iotrpi-39b89",
    'storageBucket': "iotrpi-39b89.appspot.com",
    'messagingSenderId': "381668010789",
    'appId': "1:381668010789:web:1e23343cfbeb73759b88cc",
    'measurementId': "G-4M0M5PSDMS"
}
firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()


popp=db.get()
print(popp.val())

lis=KrijoModulet().elementetLS(popp)
print(lis)
Leds=KrijoModulet().elementetLed(popp)
Sens=KrijoModulet().elementetSensor(popp)
print(Leds,Sens)

#Krijo listen e pineve per ledet dhe inicializoje ato.
PinLed=KrijoModulet().ElementetBorditLed(Leds)

#Krijo listen e pineve per sensoret dhe inicializoje ato.
PinSens=KrijoModulet().ElementetBorditSensor(Sens)

while True:
    LedValuesFromFirebase=db.child("IoTproject").child("Led").get().val()
    KrijoModulet().AkuiziLed(LedValuesFromFirebase)
    tipiSensoreveFromFirebase=db.child("IoTproject").child("tipiSensorit").get().val()
    vleratLexuarNgaSensoret=KrijoModulet().LeximiTipitTeSensoreve(tipiSensoreveFromFirebase)
    SensRilexuar=KrijoModulet().rishikimi(vleratLexuarNgaSensoret,Sens)
    db.child("IoTproject").child("Sensors").update(SensRilexuar)
    time.sleep(3.0)
    





#asa=list(popp.val())
#print(list(db.child(asa[0]).get().val()))
#number_of_leds=len(popp.val())

#for i in range(number_of_leds):
#   led_array_.append("Turn"+str(i+1))

#print(led_array_)

#led_values=[]
#for i in range(number_of_leds):
#   led_values.append(popp.val()[led_array_[i]])
#    print(i)

#print(led_values)

#auth=firebase.auth()
#storage=firebase.storage()

#login in as a user
#email="xhoixhafa@xhoi.com"
#password="12345678"
#try:

#    auth.sign_in_with_email_and_password(email,password)
#    print("login succesfull")
#except:
#    print("login not succesfull")


#email=input("enter your email")
#password=input("enter your password")

#try:
#   auth.create_user_with_email_and_password(email,password)
#   print("user created")
#except:
#    print("user alredy is created")


#storage

#filename=input("enter the file: ")
#cloudNameFile=input("enter the name of the file on the cloud")
#storage.child(cloudNameFile).put(filename)

#print(storage.child(cloudNameFile).get_url(None))


# download a file
#cloudNameFile=input("enter the name of the file on the cloud")
#storage.child(cloudNameFile).download("","voyage.txt")


#cloudNameFile=input("enter the name of the file on the cloud")
#url=storage.child(cloudNameFile).get_url(None)
#f=urllib.request.urlopen(url).read()
#print(f)



#realtime database
#data={'age':40,'address':'New York', 'employe':True, 'name':'John Smith'}
#db.child("kompan").child("myonwid").set(data)


#update
#db.child("kompan").child("myonwid").update({'name':'Mark'})

#people=db.child("kompan").get()

#for person in people.each():
#    if person.val()['name']=='mark':
#        db.child("kompan").child(person.key()).update({'name':'Jane'})


#delete
#db.child("person").child("name").remove()

#people=db.child("person").get()

#for perso in people.each():
#   if perso.val()=='ra':
#       db.child("person").child(perso.key()).child("lo").remove()

#led_array_=[]