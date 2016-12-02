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
        self.className = "Fix."
        methodName = "__init__:  "
        self.sightingFile = None
        self.logFileName = None
        self.settedAriesFile = 0
        self.settedStarsFile = 0
        self.sightingErrors = 0

        if (not(isinstance(logFile,str))) or (len(logFile) < 1 ):
            raise ValueError(self.className + methodName + "invalid value")
        self.logFileName =logFile
        try:
            self.writeLogEntry(self.logFileName,"Start of log")
        except:
            raise ValueError(self.className + methodName + "can not open or write into")          
        return 



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
            



    def getSightings(self,assumedLatitude = '0d0.0', assumedLongitude = "0d0.0"):
        methodName = "getSightings:  "
        self.approximateLatitude = "0d0.0"
        self.approximateLongitude = "0d0.0"
#        returnResult = (self.approximateLatitude,self.approximateLongitude)
        assumedLatitudeAngle = self.dealAssumedLatitude(assumedLatitude)
        assumedLongitudeAngle = self.dealAssumedLongitude(assumedLongitude)
        if assumedLatitudeAngle == 0:
            raise ValueError(self.className + methodName +"invalid assumedLat " )
        if assumedLongitudeAngle == 0:
            raise ValueError(self.className + methodName +"invalid assumedLong ")
        
        if self.settedAriesFile == 0 or self.settedStarsFile == 0:
            raise ValueError(self.className + methodName + "invalid files")

        
        valueList = []
    
        if(self.setSightingFile == None):
            raise ValueError(self.className + methodName + "not exist sightingFile")
        entryString = ""
        xmlFile = open(self.sightingFile)
        xmlFileLines = xmlFile.readlines()
        xmlFileString = ""
        for xmlFileLine in xmlFileLines:
            xmlFileString = xmlFileString + xmlFileLine
        dom = xml.dom.minidom.parse('sightings.xml')
        dom.toprettyxml()
        sightingTree = dom.documentElement
        sightingList = dom.getElementsByTagName('sighting')

        
        sumCosForEachSighting = 0
        sumSinForEachSighting = 0
        for sighting in sightingList:
            resultHandle = self.handleDomTree(sighting)
            if resultHandle == 0:
                self.sightingErrors+=1
            else:
                if not self.body == "unknown":
                    entryString = self.entryHeader()
                    adjustedAltitude = self.ulateAdjustedAltitude()
                    adjustedAltitudeAngle = Angle.Angle()
                    adjustedAltitudeAngle.setDegrees(adjustedAltitude)
                    adjustedAltitudeAngleString = adjustedAltitudeAngle.getString()
                    adjustedAltitudeDegree = adjustedAltitudeAngle.getDegrees()
                
                entryString += self.body + "\t"  
                entryString += self.date + "\t"
                entryString += self.time + "\t"  
                entryString +=str(adjustedAltitudeAngleString) + "\t"
                gha = self.getGHA()
                
                geographicPositionLatitudeAngle = Angle.Angle()
                geographicPositionLongitudeAngle = Angle.Angle()
                
                geographicPositionLatitudeAngle.setDegreesAndMinutes(gha[0])
                geographicPositionLongitudeAngle.setDegreesAndMinutes(gha[1])
                
                geographicPositionLatitudeDegree = geographicPositionLatitudeAngle.getDegrees()
                geographicPositionLongitudeDegree = geographicPositionLongitudeAngle.getDegrees()
                 
                entryString += gha[0] + "\t" +gha[1] + "\t"
                entryString += assumedLatitude + "\t" + assumedLongitude +"\t"
                
                LHAAngle = Angle.Angle()
                LHAAngle.setDegrees(geographicPositionLongitudeDegree)
                LHAAngle.add(assumedLongitudeAngle)
                LHA = LHAAngle.getDegrees()
                
                
                sinLat1 = math.sin(math.radians(geographicPositionLatitudeAngle.getDegrees()))
                print "sinLat1: "+str(sinLat1)  
                  
                sinLat2 = math.sin(math.radians(assumedLatitudeAngle.getDegrees()))
                print "sinLat2: "+str(sinLat2) 
                sinLat = sinLat1 * sinLat2
                print "sinLat: "+str(sinLat)
                
                cosLat1 = math.cos(math.radians(geographicPositionLatitudeAngle.getDegrees()))
                print "cosLat1: "+str(cosLat1) 
                cosLat2 = math.cos(math.radians(assumedLatitudeAngle.getDegrees()))
                print "cosLat2: "+str(cosLat2)
                cosLHA = math.cos(math.radians(LHA))
                print "cosLHA: "+str(cosLHA)
                cosLat = cosLat1 * cosLat2 * cosLHA
                print "cosLat: "+str(cosLat)
                intermediateDistance = sinLat + cosLat
                print "intermediateDistance: "+ str(intermediateDistance)
                correctedAltitude = math.asin(intermediateDistance)
                print "correctedAltitude: " +str(correctedAltitude)

  
                #-------
                distanceAdjustmentFloat = 60*(math.degrees(correctedAltitude) - adjustedAltitudeDegree)
                distanceAdjustmentInteger = round(distanceAdjustmentFloat)
                print "distance adjustment (before round): "+str(distanceAdjustmentFloat), "*"*30 , "distance"
                print "distance adjustment: "+str(distanceAdjustmentInteger), "*"*30 , "distance"
                
                #-------
                print "D: =================================="
                theNumerator = sinLat1 - sinLat2 * intermediateDistance
                print "numerator: "+str(theNumerator)
                cosLat1 = math.cos(math.radians(assumedLatitudeAngle.getDegrees()))
                print "cosLat1: "+str(cosLat1)
                cosLat2 = math.cos(correctedAltitude)
                print "cosLat2: "+str(cosLat2)
                theDenominator = cosLat1 * cosLat2
                print "denominator: "+str(theDenominator)
                intermediaAzimuth = theNumerator / theDenominator
                print "intermedia azimuth: "+str(intermediaAzimuth)
                azimuthAdjustment = math.acos(intermediaAzimuth)
                print "azimuth adjustment(rad): "+str(azimuthAdjustment)
                azimuthAdjustmentAngle = Angle.Angle()
                
                azimuthAdjustmentAngle.setDegrees(math.degrees(azimuthAdjustment))
                print "azimuth adjustment: "+azimuthAdjustmentAngle.getString(), "*"*30 , "azimuth"
                entryString += azimuthAdjustmentAngle.getString() + "\t" + str(distanceAdjustmentInteger) +"\t"               
                    
                sumCosForEachSighting += distanceAdjustmentInteger * math.cos(math.radians(azimuthAdjustmentAngle.getDegrees()))
                sumSinForEachSighting += distanceAdjustmentInteger * math.sin(math.radians(azimuthAdjustmentAngle.getDegrees()))
                
                self.logFile.write(entryString+"\n")
                self.logFile.flush()
                
                entryString = ""
                
#                 else:
#                     self.sightingErrors+=1
            
        print"\n"
        print "distance adjustment * cos(azimuth adjustment) = "+ str(sumCosForEachSighting)
        print "distance adjustment * sin(azimuth adjustment) = "+ str(sumSinForEachSighting)
        
        self.approximateLatitude = assumedLatitudeAngle.getDegrees() + sumCosForEachSighting / 60   
        print "assumedLatitudeAngle.getDegrees() = "+str(assumedLatitudeAngle.getDegrees())
        print "sumCosForEachSighting / 60 = "+str(sumCosForEachSighting / 60)
        
        if self.approximateLatitude>=270 and self.approximateLatitude<=360:
            self.approximateLatitude = self.approximateLatitude - 360
            
        if self.approximateLatitude>90 and self.approximateLatitude<270:    
            self.approximateLatitude = 180 - self.approximateLatitude
            
        self.approximateLongitude = assumedLongitudeAngle.getDegrees() + sumSinForEachSighting / 60       
            
        approximateLatitudeString = str(int(self.approximateLatitude))+"d"+ str(abs(round((self.approximateLatitude-int(self.approximateLatitude))*60,1)))
        if self.approximateLatitude<0:
            approximateLatitudeString = approximateLatitudeString.replace("-","S")
        else:
            approximateLatitudeString = "N" + approximateLatitudeString
            
        approximateLongitudeAngle = Angle.Angle()
        approximateLongitudeAngle.setDegrees(self.approximateLongitude)
        self.returnApproximateLatitude = approximateLatitudeString
        self.returnApproximateLongitude = approximateLongitudeAngle.getString()
        self.EndOfLog()
        
        return (self.returnApproximateLatitude, self.returnApproximateLongitude)   
                   
            
        
            
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
        prefix +=tab
        return prefix
          
        
    def setAriesFile(self,ariesFile = 0):
        methodName = "setAriesFile: "
        entryString = ''
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
        ariesFilePath = os.path.abspath(ariesFile)
        entryString = "Aries file:\t" + self.ariesFilePath
        self.writeLogEntry(entryString)
        self.ariesFileName.close()
        self.settedAriesFile = 1
        return ariesFilePath 
    
    
    
    
    
    def setStarFile(self,starFile = 0):
        methodName = "setStarFile: "
        entryString = ''
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
    
    
    def dealAssumedLatitude(self,assumedLatitude):
        methodName = "dealAssumedLatitude"
        if"-" in assumedLatitude:
            print"Fix.dealAssumedLatitude() -1"
            return 0
        
        if("N" not in assumedLatitude) and ("s" not in assumedLatitude):
            if assumedLatitude != "0d0.0":
                print"Fix.dealAssumedLatitude() - 2"
                return 0
        
        if "N" in assumedLatitude:
            assumedLatitude = assumedLatitude.replace("N","")
        if "S" in assumedLatitude:
            assumedLatitude = assumedLatitude.replace("S","-")
            
        if"0d0.0"in assumedLatitude:
            if"N" in assumedLatitude or "S" in assumedLatitude:
                print "Fix.dealAssumedLatitude() - 3"
                return 0
        assumedLatitudeAngle = Angle.Angle()
        
        try:
            assumedLatitudeAngle.setDegreesAndMinutes(assumedLatitude)
        except:
            print"Fix.dealAssumedLatitude() -4"
            return 0
        assumedLatitudeArray = assumedLatitude.split("d")
        print"assumed:atitudeArray[0] = "+assumedLatitudeArray[0]
        if float(assumedLatitudeArray[0]>=90 or float(assumedLatitudeArray[0])<=-90):
            print"Fix.dealAssumedLatitude() - 5"
            return 0
    
        return assumedLatitudeAngle
    
    def dealAssumedLongtitude(self,assumedLongitude):
        
        assumedLongitudeAngle = Angle.Angle()
        try:
            assumedLongitudeAngle.setDegreesAndMinutes(assumedLongitude)
        except:
            return 0
        
        return assumedLongitudeAngle
    
    
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
        print "aries1GHA: " + ariesGHA1.getString()
        
        timeArray = self.time.split(':')
        s = float(timeArray[1])*60 + float(timeArray[2])
        
        m = ariesGHA2.subtract(ariesGHA1)* (s/3600)
        ariesGHA = ariesGHA1.getDegrees() + m
        print"ariesGHA: "+str(ariesGHA)
        print"starSHA: "+str(starSHA)
        observationGHA = ariesGHA + starSHA
        observationGHAAngle = Angle.Angle()
        observationGHAAngle.setDegrees(observationGHA)
        geoPosLatitude = observationGHAAngle.getString()
        return(geoPosLatitude , geoPosLongitude)
        
        
        
    def getStarsFile(self):
        methodName = "getStarsFile: "
        
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
        methodName = "getAriesFile: "
        self.ariesFile = open(self.ariesFileName)
        ariesFileEntries = self.ariesFile.readlines()
        ariesEntryDic1 = {}
        tag = 0
        for ariesFileEntries in ariesFileEntries:
            ariesFileLineArray = ariesFileEntries.split()
            date1 = time.strptime(self.date, "%Y-%m-%d")
            time1Array = self.time.split(":")
            time1 = int(time1Array[0])
            date2 = time.strptime(ariesFileLineArray[0], "%m/%d/%y")
            time2 = int(ariesFileLineArray[1])
            
            if tag == 1:
                ariesEntryDic2 = {'date': ariesFileLineArray[0],
                            'hour': ariesFileLineArray[1],
                             'gha': ariesFileLineArray[2]}
                return ariesEntryDic1, ariesEntryDic2
            
            if date1 == date2 and time1 == time2:
                if tag == 0:
                    ariesEntryDic1 = {'date': ariesFileLineArray[0],
                                'hour': ariesFileLineArray[1],
                                'gha': ariesFileLineArray[2]}
                    tag = tag + 1
        if tag == 0:
            return 0

                       

        
        