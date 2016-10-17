from xml.dom.minidom import parse 
from datetime import datetime
from xml.dom import minidom as minidom
from time import  strftime
import math
import Angle


class Fix():
   
    def __init__(self,logFile="log.txt"):
        self.logFile = logFile
        self.setSightingFile = None
        dateTime= strftime("%Y-%m-%d %H:%M:%S")
        self.sightingHeader = "LOG:\t"
        self.className = "Fix."
        
        methodName = "__init__:  "
        if (not(isinstance(logFile,str))) or (len(logFile) < 1 ):
            raise ValueError(self.className + methodName + "invalid value"  )
        try:
            with open(self.setSightingFile , 'w','r','a') as f:
                f.write(self.sightingHeader +dateTime+"\tStart of log\n")
                f.read(self.setSightingFile)
                f.append(self.setSightingFile)
        except:
            raise ValueError(self.className + methodName + "invalid value")

           
#     def readAndWritelogInFile(self,logFile):   
#         with open('logFile' , 'w','r','a') as f:
#             f.write("Start of log")
#             f.read("logFile")
#             f.append("logFile")

    def setSightingFile(self,sightingFile):
        self.setSightingFile = sightingFile
        methodName = "setSightingFile:  "
        if(not(isinstance((self.setSightingFile), str))) or (len(self.setSightingFile) < 1):
            raise ValueError(self.className + methodName + "invalid value" )
        try:
            t = len(self.setSightingFile)
            n = self.setSightingFile.find(".XML")
            if (n!=t-len(".XML"))|(t-len(".XML")<1):
                raise ValueError(self.className + methodName + "invalid value")
            with open(self.setSightingFile, 'w','r','a') as f:
                f.write(self.sightingHeader+datetime +"\tStart of sighting file f.xml\n")
                f.read(self.setSightingFile)
                f.append(self.setSightingFile)
        except:
                raise ValueError(self.className + methodName + "invalid value")    
            
        return self.setSightingFile

    def getSettings(self,getSettings):
        methodName = "getSettings "
        self.approximateLatitude = "0d0.0"
        self.approximateLongitude = "0d0.0"
        if(self.setSightingFile == None):
            raise ValueError(self.className + methodName + "not exist sightingFile")
        
        dom = parse(self.setSightingFile)
        bodyJudge = len(dom.getElementsByTagName("body")[0].childNodes[0])
        if (len(bodyJudge) == 0):
            raise ValueError(self.classname + methodName + "no body in file" )
        
        dateJudge = len(dom.getElementsByTagName("date")[0].childNodes[0])
        if (len(dateJudge) == 0):
            raise ValueError(self.classname + methodName + "no date in file" )
        
        timeJudge = len(dom.getElementsByTagName("time")[0].childNodes[0])
        if (len(timeJudge) == 0):
            raise ValueError(self.classname + methodName + "no time in file" )
        
        observationJudge = len(dom.getElementsByTagName("observation")[0].childNodes[0])
        if (len(observationJudge) == 0):
            raise ValueError(self.classname + methodName + "no observation in file" )
        
        heightJudge = len(dom.getElementsByTagName("height")[0].childNodes[0])
        if (len(heightJudge) == 0):
            theHeight  = 0
        else:
            theHeight = dom.getElementsByTagName("height")[0].childNodes[0].data
            
        temperatureJudge = len(dom.getElementsByTagName("temperature")[0].childNodes[0])
        if (len(temperatureJudge) == 0):
            theTemperature = 70
        else:
            theTemperature = dom.getElementsByTagName("temperature")[0].childNodes[0].data
            
        pressureJudge = len(dom.getElementsByTagName("pressure")[0].childNodes[0])
        if (len(pressureJudge) == 0):
            thePressure = 1010
        else:
            thePressure = dom.getElementsByTagName("pressure")[0].childNodes[0].data
            
        horizonJudge = len(dom.getElementsByTagName("horizon")[0].childNodes[0])
        if (len(horizonJudge) == 0):
            theHorizon = 'natural'
        else:
            theHorizon = dom.getElementsByTagName("horizon")[0].childNodes[0].data
            
     
        doc = minidom.parse(self.setSightingFile)
        body0 = doc.getElementsByTagName("body")[0].childNodes[0].data
        date0 = doc.getElementsByTagName("date")[0].childNodes[0].data
        time0 = doc.getElementsByTagName("time")[0].childNodes[0].data
        observation0 = doc.getElementsByTagName("observation")[0].childNodes[0].data
        body1 = doc.getElementsByTagName("body")[1].childNodes[0].data
        date1 = doc.getElementsByTagName("date")[1].childNodes[0].data
        time1 = doc.getElementsByTagName("time")[1].childNodes[0].data
        observation1 = doc.getElementsByTagName("observation")[1].childNodes[0].data
        
        try:
            with open(self.setSightingFile, 'w') as f:
                f.write(self.sightingHeader+datetime+body0+date0+time0+observation0)
                f.write(self.sightingHeader+datetime+body1+date1+time1+observation1)
        except:
            raise ValueError(self.className + methodName + "invalid value")
        return (self.approximateLatitude, self.approximateLongitude)

    def FahrenheitToCelsius(self, fahrenheit):
        celsius = (float(fahrenheit) - 32 ) / 1.8
        return celsius    
        
 
    def calculateAdjustAttitude(self, height,pressure,obHorizon,temperature,observedAltitude):
        dom = parse(self.setSightingFile)
        height = dom.getElementsByTagName("horizon")[0].childNodes[0].data
        if ( height== 'natural'):
            dip = (-0.97 * math.sqrt(height)) / 60.0
        else:
            dip = 0
        
        refraction = (-0.00452 * float(pressure))/(273 + self.FahrenheitToCelsius(temperature)) /math.atan(observedAltitude)
        adjustedAttitude = round(observedAltitude + dip + refraction)
        return adjustedAttitude 
        
        
        
        
        
        
        