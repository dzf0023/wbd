from xml.dom.minidom import parse 
from datetime import datetime,date,timedelta,tzinfo
#from xml.dom import minidom as minidom
from time import  strftime,strptime
import math
import Angle
import xml.dom.minidom
import  os
import time
class TZ(tzinfo):
    def utcoffset(self, dt):
        return tzinfo.timedelta(minutes = -6*60)
class Fix():
   
    def __init__(self,logFile="log.txt"):
        self.logFile = logFile
        self.sightingFile = None
#         dateTime= strftime("%Y-%m-%d %H:%M:%S")
        self.sightingHeader = "LOG:\t"
        self.className = "Fix."
        self.logFileName = None
        methodName = "__init__:  "

        if (not(isinstance(logFile,str))) or (len(logFile) < 1 ):
            raise ValueError(self.className + methodName + "invalid value")
#        self.starFileName = starFile
        self.logFileName =logFile
        try:
            self.writeLogEntry("Start of log")
        except:
            raise ValueError(self.className + methodName + "can not open or write into")          




    def setSightingFile(self,sightingFile = None):
        self.sightingFile = sightingFile
        dateTime= strftime("%Y-%m-%d %H:%M:%S")
        methodName = "setSightingFile:  "
        begin = "Start of sighting file "
        if(not(isinstance((self.sightingFile), str))) or (len(self.sightingFile) < 1):
            raise ValueError(self.className + methodName + "wrong type of value" )
        if(self.sightingFile.find(".")==-1):
            raise ValueError(self.className +methodName + "invalid file name")    
        
        t = len(self.sightingFile)
        n = self.sightingFile.find(".xml")
        
        if (n!=t-len(".xml")) or (t-len(".xml")<1):
            raise ValueError(self.className + methodName + "invalid value")
        self.logFileName = 'sightings.xml'
        try:
            sightingFileInstance = open(self.sightingFile, 'r')
            sightingFileInstance.close()
            self.writeLogEntry(begin + self.sightingFile)
            sightingFilepath = os.path.abspath("sightings.xml")
        except:
            raise ValueError(self.className + methodName + "invalid value111")    
        return sightingFilepath
            



    def getSightings(self):
        methodName = "getSightings:  "
        self.approximateLatitude = "0d0.0"
        self.approximateLongitude = "0d0.0"
#        returnResult = (self.approximateLatitude,self.approximateLongitude)
        
        valueList = []
    
        if(self.setSightingFile == None):
            raise ValueError(self.className + methodName + "not exist sightingFile")
        
        dom = xml.dom.minidom.parse('sightings.xml')
        sightingList = dom.getElementsByTagName('sighting')
        for sighting in sightingList:
            valueList.append(self.obtainSightingValues(sighting))
        return valueList

    
    def obtainSightingValues(self,dom):
        try:
            bodyValue = self.extractValueByTag(dom,"body")
            dateValue = self.extractValueByTag(dom, "date") 
            timeValue = self.extractValueByTag(dom, "time")
            observationValue = self.extractValueByTag(dom, "observation")
            heightValue = self.extractValueByTag(dom, "height", True, "0.0")
            self.validateHeightValue(heightValue)
            pressureValue = self.extractValueByTag(dom, "pressure", True, "1010")
            self.validatePressureValue(pressureValue)
        except:
            raise ValueError
        return [bodyValue,dateValue,timeValue,observationValue, heightValue, pressureValue]
            
    
    
    
    
    
    def extractValueByTag(self,dom,tagName,optional = False , defaultValue= 0):
        subDomList = dom.getElementsByTagName(tagName)
        if(len(subDomList) == 0):
            if(optional):
                return defaultValue
            raise ValueError
        childNodes = subDomList[0].childNodes
        tagValue = ''
        for child in childNodes:
            if(child.nodeType == child.TEXT_NODE):
                tagValue += child.data
        return tagValue

    def calculateFahrenheit(self, fahrenheit):
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
        
        
        
    def validateHeightValue(self, h):
        try:
            if(float(h) < 0.0):
                raise ValueError
        except:
            raise ValueError
    
    
    def validatePressureValue(self, p):
        integerPressure = int(p) 
        if(integerPressure < 100) or (integerPressure > 1100):
            raise ValueError
#    Function Method
    def writeLogEntry(self,entry):
        newLine = '\n'
        openedFile = open(self.logFileName,'a')
        logEntry = self.buildPrefix()
        logEntry += entry
        logEntry += newLine
        openedFile.write(logEntry)
        openedFile.close()
             
    def buildPrefix(self):
        tab = "\t"
        prefix = "LOG: "
        timeGet = datetime.now()
        prefix += datetime(timeGet.year, timeGet.month, timeGet.day, timeGet.hour,timeGet.minute,timeGet.second,tzinfo=TZ().isoformat(tab))
          
        
    def setAriesFile(self,ariesFile = None):
        methodName = "setAriesFile: "
#        entryString = ''
        self.ariesFileName = ariesFile
        if(not(isinstance(ariesFile,str))):
            raise ValueError(self.className + methodName + "invalidAries name")
        if(ariesFile.find(".") == -1):
            raise ValueError(self.className + methodName + "invalidAries name")
        parseName = ariesFile.split(".")
        if(len(parseName[0] )< 1):
            raise ValueError(self.className + methodName + "invalidAries name")
        if(parseName[-1].lower() !="txt"):
            raise ValueError(self.className + methodName + "invalidAries name")
        try:
            ariesFileInstance = open(ariesFile,'r')
            ariesFileInstance.close()
            self.ariesFileName = ariesFile
        except:
            raise ValueError(self.className + methodName + "invalid name")
        ariesFilePath = os.path.abspath('aries.txt')
        self.starFile.close()
        return ariesFilePath 
    
    
    
    
    def setStarFile(self,starFile):
        methodName = "setStarFile: "
#        entryString = ''
        self.starFileName = starFile
        if(not(isinstance(starFile,str))):
            raise ValueError(self.className + methodName + "invalidStars name")
        if(starFile.find(".") == -1):
            raise ValueError(self.className + methodName + "invalidStars name")
        parseName = starFile.split(".")
        if(len(parseName[0] )< 1):
            raise ValueError(self.className + methodName + "invalidStars name")
        if(parseName[-1].lower() !="txt"):
            raise ValueError(self.className + methodName + "invalidStars name")
        try:
            starsFileInstance = open(starFile,'r')
            starsFileInstance.close()
            self.starFileName = starFile
        except:
            raise ValueError(self.className + methodName + "invalid name")
        starsFilePath = os.path.abspath("stars.txt")
        self.setStarFile.close()
        return starsFilePath
    
    # quote from GitHub
    def getGHA(self,ang):
        methodName = "getGHA: "
        # find the angular displacement of the stars relative to Aries 
        star = self.findStars()
        if(star == -1):
            raise ValueError(self.className + methodName + "can not find information in stars.txt")
        aries = self.findAries()
        if(aries == -1):
            raise ValueError(self.className + methodName + "can not find information in aries")
        
        geoPosLatitude = star['latitude']
        geoPosLongitude= star['longitude']
        starSHAAngle = Angle.Angle()
        starSHAAngle.setDegreesAndMinutes("stars.txt")
        starSHA = starSHAAngle.getDegrees()
        
        ariesGHA1 = Angle.Angle()
        ariesGHA2 = Angle.Angle()
        ariesGHA1.setDegreesAndMinutes(aries[0]['gha'])
        ariesGHA2.setDegreesAndMinutes(aries[1]['gha'])
        
#         timeArray = self.time.split(':')
#         s = float(timeArray[1])*60 + float(timeArray[2])
        ariesGHA = ariesGHA1 + starSHA
        observationGHA = ariesGHA + starSHA
        observationGHAAngle = Angle.Angle()
        observationGHAAngle.setDegrees(observationGHA)
        geoPosLatitude = observationGHAAngle.getString()
        return(geoPosLatitude , geoPosLongitude)
        
        
     ## quote from GitHub   
    def getStarsFile(self):
#        methodName = "getStarsFile: "
        
        self.starsFile = open(self.starFileName)
        starFileEntries = self.starFile.readlines()
        starEntryDic = {}
        for starFileEntry in starFileEntries:
            starFileLineArray = starFileEntry.split()
            if(starFileLineArray[0]==self.body):
                dateTime1= strftime("%Y-%m-%d %H:%M:%S")
                dateTime2= strftime("%Y-%m-%d %H:%M:%S")
                if dateTime1>dateTime2:
                    starEntryDic = {'body':starFileLineArray[0],
                    'date':starFileLineArray[1],
                    'longitude':starFileLineArray[2],
                    'latitude': starFileLineArray[3]}
                else:
                    return starEntryDic
                
    def getAriesFile(self):
#   #      methodName = "getAriesFile: "
#         self.ariesFile = open(self.ariesFileName)
#         ariesFileEntries = self.ariesFile.readlines()
#         ariesEntryDic = {}
        pass
    
        
        
