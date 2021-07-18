#my project class for IoT Automation
import pyrebase
import urllib
import time
#from  dht11example import Sensori


class KrijoModulet:
    def __init__(self,popp=None,data=None):
        self.popp=popp
        data={}
    
    def listat(self,popp):
        self.popp=popp
        lista=list(popp.val())
        return lista
        
    
    def elementetListes(self,popp):
        self.popp=popp
        lista=list(popp.val())
        Elementi=popp.val()[lista[0]]
        return Elementi
    
    def elementetLS(self,popp):
        self.popp=popp
        lista=list(popp.val())
        Elementi=popp.val()[lista[0]]
        ElementiLS=list(Elementi)
        return ElementiLS

    def elementetLed(self,popp):
        self.popp=popp
        lista=list(popp.val())
        Elementi=popp.val()[lista[0]]
        ElementiLS=list(Elementi)
        if ElementiLS[0]=='Led':
            VleratLed=Elementi[ElementiLS[0]]
            return VleratLed
        else:
            print("Fusha e ledeve ka problem")
    
    def elementetSensor(self,popp):
        self.popp=popp
        lista=list(popp.val())
        Elementi=popp.val()[lista[0]]
        ElementiLS=list(Elementi)
        if ElementiLS[1]=='Sensors':
            VleratSensor=Elementi[ElementiLS[1]]
            return VleratSensor
        else:
            print("Fusha e ledeve ka problem")
    
    def ElementetBorditLed(self,Leds):
        self.Leds=Leds
        ListaLed=list(Leds)
        dictonOfLeds={
            'Pin14':14,
            'Pin18':18,
            'Pin19':19
        }
        lengthOfLeds=len(ListaLed)
        PinetLed=[]
        for i in range(0,lengthOfLeds):
            PinetLed.append(dictonOfLeds[ListaLed[i]])
        
        for i in range(0,lengthOfLeds):
            #GPIO.setup(PinetLed[i],GPIO.OUT)
            pass
        return PinetLed
    
    def ElementetBorditSensor(self,Sens):
        self.Sens=Sens
        ListaSens=list(Sens)
        dictonOfSensor={
            'Pin15':15,
            'Pin17':17,
            'Pin11':11
        }
        lengthOfSens=len(ListaSens)
        PinetSens=[]
        for i in range(0,lengthOfSens):
            PinetSens.append(dictonOfSensor[ListaSens[i]])
        
        for i in range(0,lengthOfSens):
            #GPIO.setup(PinetLed[i],GPIO.IN)
            pass
        return PinetSens

    
    def AkuiziLed(self,LedValuesFromFirebase):
        self.LedValuesFromFirebase=LedValuesFromFirebase
        dictonOfLeds={
            'Pin14':14,
            'Pin18':18,
            'Pin19':19
        }
        LeximiLedLista=list(LedValuesFromFirebase)
        
        for i in range(0,len(LeximiLedLista)):
            if LedValuesFromFirebase[LeximiLedLista[i]]=='on':
                #GPIO.output(dictonOfLeds[LeximiLedLista[i]], GPIO.HIGH)
                print("true")
                
            elif LedValuesFromFirebase[LeximiLedLista[i]]=='off':
                #GPIO.output(dictonOfLeds[LeximiLedLista[i]], GPIO.LOW)
                print("false")
            
            else:
                print("There is a problem with reading the values of leds")

    
    def LeximiTipitTeSensoreve(self,tipiSensoreveFromFirebase):
        self.tipiSensoreveFromFirebase=tipiSensoreveFromFirebase
        ListaPineve=list(tipiSensoreveFromFirebase)
        vleratLexuara=[]
        dictonOfSensor={
            'Pin15':15,
            'Pin17':17,
            'Pin11':11
        }
        for i in range(0,len(ListaPineve)):
            if tipiSensoreveFromFirebase[ListaPineve[i]]=="DHT11":
               vleratLexuara.append(12) #Sensori().SensoriDHT(dictonOfSensor[ListaPineve[i]])
               print("hi")
            else:
                vleratLexuara.append("error - 404")
        return vleratLexuara
    
    def rishikimi(self,vleratLexuarNgaSensoret,Sens):
        self.vleratLexuarNgaSensoret=vleratLexuarNgaSensoret
        self.Sens=Sens
        for i in range(0,len(vleratLexuarNgaSensoret)):
            if len(vleratLexuarNgaSensoret[i])==1:
                Sens[list(Sens)[i]]=vleratLexuarNgaSensoret[i]
            else:
                Sens[list(Sens)[i]]=vleratLexuarNgaSensoret[i]
                for j in range(0,len(Sens)):
                    if j==0:
                        Sens[j]={'humidity':vleratLexuarNgaSensoret[i][j]}
                    elif j==1:
                        Sens[j]={'temp':vleratLexuarNgaSensoret[i][j]}

                       


            
        
        return Sens
        
    

    

        
    



    


     

    

