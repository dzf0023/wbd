'''
Created on Oct 10, 2016

@author: dongjifeng
'''
import unittest
import Navigation.prod.Fix as Fix
# from matplotlib.font_manager import path
# from scipy.odr.odrpack import Output
# from pydoc import classname
import os 

class FixTest(unittest.TestCase):
    
    def setUp(self):
        self.className = "Fix."
        try:
            os.remove("log.txt")
        except:
            pass
        
    def tearDown(self):
        pass
    
#    Acceptance Test:100
#        Analysis - Fix(logFile)
#        inputs
#           logFile   expressed as string, length.GE.1.  Optional
#        outputs
#            instance of Fix
#            default to "log.txt" if missing
#        state change 
#            should entry "start of log" to the log file
#
#        Happy path:
#            omitted  Fix()
#           nominal case for string and .GE.1:  Fix(logFile= "logOfStar")
#           nominal case for nothing            Fix(logFile= "log.txt")
#        sad path
#           nominal case for (no string )float or integer        Fix(logFile= "111") & Fix(logFile = "11.11")
#
#        Happy path
    def test100_010_ShouldCreatInstanceOfFix(self):
        self.assertIsInstance(Fix.Fix(),Fix.Fix)
        
    def test100_020_ShouldConstructFixWithDefaultFile(self):
        theFix = Fix.Fix()
        myLogFile = open("setSightingFile",'r')
        entry = myLogFile.readline()
        self.assertNotEqual(-1,entry.find("Start of log\n"))
        self.assertInstance(theFix,Fix.Fix)
        
#       os.remove("self.setSightingFile")
 
        

#        sad path
    def test100_030_ShouldRaiseExceptionOnNonNameLogFile(self):
        expectedDiag = self.className + "setSightingFile:  "
        theFix = Fix.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile("")
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)]) 
        
    def test100_040_ShouldRaiseExceptionOnIntegerFileNameParm(self):
        expectedDiag = self.className + "setSightingFile:  "
        theFix = Fix.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile(123)
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)]) 
        
#    Acceptence Test:200
#        Analysis - setSettingFile
#            inputs
#                settingFileString : string in from of f.xml
#                        f is file name .GE.1 
#                    a  new  file .  boolean value =True      already exist. boolean value = False
#            outputs
#               string value
#                write following entry to the log file
#                    Star of sighting file f.xml
#                    where f.xml is actual name of the file 
#            happy path:
#                nominal case: setSettingFile() for  logFile.xml
#            sad path 
#                    none*
#        Happy path
    def test200_010_ShouldReturnSightingFile(self):
        expectedName = "dj.xml"
        theFix = Fix.Fix()
        returnedValue = theFix.setSightingFile(expectedName)
        self.assertEqual(expectedName,returnedValue)
         
    def test200_020_ShouldWriteEntryofSightingFile(self):
        theFix = Fix.Fix()
        theFix.setSightingFile("sightings.xml")
        myLogFile = open("log.txt",'r')
        entry = myLogFile.readlines()
        self.assertNotEqual(-1,entry[1].find("Start of sighting file"))

#       Sad path
    def test200_020_ShouldRaiseExceptionOnNonStringForm(self):
        theFix = Fix.Fix()
        with self.assert_(ValueError) as context:
            theFix(123)
                
    def test200_030_ShouldRaiseExceptionOnFLenLessThan1(self):   
        theFix = Fix.Fix()
        with self.assert_(ValueError) as context:
            theFix(".XML")
        
    def test200_040_ShouldRaiseExceptionOnWrongPosition(self):
        theFix = Fix.Fix()
        with self.assert_(ValueError) as context:
            theFix("aaa.XMLaaa")
                
                

#    Acceptence Test:300
#        Analysis-getSettings
#            Inputs 
#                 no params 
#            Outputs
#                (approximateLatitude, approximateLongitude)
#                    a tuple with ('0d0','0d0')
#            state change:
#            Navigation Calculation are written into the log file 
#       
#         Happy  path 
#            nominal case for return(0d0.0 , 0d0.0)
#            nominal case with default log.txt has contents write into the logFile"
#            nominal case with given logFile for "end of sighting file "be written  into the log file"
#            nominal case  log are sorted and written in 
#
#       Sad path
#                no sightingFile has been set 
#                lose mandatory tag in sighting file 
#                     fix not exist 
#                    no sightingFile exist 
#                     sighting   
#                    body missing 
#                    date missing ,
#                    time  missing 
#                     observation missing 
#                        height content is not numeric 
#                     height has not limited 
#                 invalid information in tag     
#                a sighting file has more than one "<fix>" tag
#                temperature content is not an integer 
#                pressure content is not an integer 
#            pressure content is an integer , without in the limited  range 
#``            observation content is .LT. 0d0.1
#
#        the observed altitude  is not  LT.0.1 arc-minutes
#
#       Happy path
    def test300_010_ShouldExtractBodyInfoFromSightingFile(self):
        theFix = Fix.Fix()
        approximatePosition = theFix.getSightings()
        self.assertListEqual(("0d0","0d0"), approximatePosition)
        
 
       
       
    def test300_020_ShouldExtractDateInfoFromSightingFile(self):
        theFix = Fix.Fix()
        self.assertEqual(2016-03-01,theFix.getSettings)
    
    def test300_030_ShouldExtractTimeInfoFromSightingFile(self):
        theFix = Fix.Fix()
        self.assertEqual('23:40:01',theFix.getSettings)
        
    def test300_040_ShouldExtractObservationInfoFromSightingFile(self):
        theFix = Fix.Fix()
        self.assertEqual('015d04.9', theFix.getSettings)
        
    def test300_050_ShouldWriteEndofSightingFileIntoLogFile(self):
        theFix = Fix.Fix()
        theFix.getSightings()
        myLogFile = open("log.txt",'r')
        entry = myLogFile.readlines()
        self.assertNotEqual(-1,entry[-1].find("End of sighting file")) 
   
#       sad pass
    def test300_090_ShouldRaiseValueErrorOnBodyLosing(self):
        expectedDiag = self.className + "getSightings:  "
        theFix = Fix.Fix
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile("missBodyTag.xml")
            theFix.getSightings()
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)]) 
        
    def test300_910_ShouldRaiseErrorWithTimeTagMissing(self):         
        expectedDiag = self.className + "getSightings:  "
        theFix = Fix.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile("misstimetag.xml")
            theFix.getSightings()
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)])
        
    def test300_920_ShouldRaiseErrorWithDateTagMissing(self):         
        expectedDiag = self.className + "getSightings:  "
        theFix = Fix.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile("missdatetag.xml")
            theFix.getSightings()
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)]) 
        
    def test300_930_ShouldRaiseErrorWithObservationTagMissing(self):         
        expectedDiag = self.className + "getSightings:  "
        theFix = Fix.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile("observationmissing.xml")
            theFix.getSightings()
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)])   
        


    