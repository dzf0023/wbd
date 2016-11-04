'''
Created on Oct 10, 2016

@author: dongjifeng
'''
import unittest
import Navigation.prod.Fix as Fix
import os 
import uuid
class FixTest(unittest.TestCase):
    
    def setUp(self):
        self.className = "Fix."
        #set default log file name
        self.DEFAULT_LOG_FILE = "log.txt"
        try:
            if(os.path.isfile(self.DEFAULT_LOG_FILE)):
                os.remove(self.DEFAULT_LOG_FILE)
        except:
            pass

        # generate random log file name 
        self.RANDOM_LOG_FILE = "log" + str(uuid.uuid4())[-12:] + ".txt"
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
#            catch the absolute path of the log file 
#        sad path
#           nominal case for (no string )float or integer        Fix(logFile= "111") & Fix(logFile = "11.11")
#
#        Happy path
    def test100_010_ShouldCreatInstanceOfFix(self):
        self.assertIsInstance(Fix.Fix(),Fix.Fix)
                 
    def test100_020_ShouldConstructFixWithDefaultFile(self):
        theFix = Fix.Fix()
        myLogFile = open('log.txt','r')
        entry = myLogFile.readline()
        self.assertNotEqual(-1,entry.find("Start of log\n"))
        self.assertIsInstance(theFix,Fix.Fix)
              
#     def test100_230_ShouldExtractAbPathOfLogFile(self):
#         theFix = Fix.Fix()
#         myLogFile = open('log.txt','r')
#         entry = myLogFile.readline()
#         self.assertEqual(first, second, msg)
        
#  
#         
# 
#   sad path
    def test100_030_ShouldRaiseExceptionOnEmpetyLogFile(self):
        expectedDiag = self.className + "__init__:  "
        theFix = Fix.Fix()
        with self.assertRaises(ValueError) as context:
            Fix.Fix('')
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)]) 
         
    def test100_040_ShouldRaiseExceptionOnIntegerFileNameParm(self):
        expectedDiag = self.className + "__init__:  "
#        theFix = Fix.Fix()
        with self.assertRaises(ValueError) as context:
            Fix.Fix(111)
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)]) 
  
       
# #    Acceptence Test:200
# #        Analysis - setSettingFile
# #            inputs
# #                settingFileString : string in from of f.xml
# #                        f is file name .GE.1 
# #                    a  new  file .  boolean value =True      already exist. boolean value = False
# #            outputs
# #               string value
# #                write following entry to the log file
# #                    Star of sighting file f.xml
# #                    where f.xml is actual name of the file 
# #            happy path:
# #                nominal case: setSettingFile() for  logFile.xml
# #            sad path 
# #                    sightingFile:
#                        null ;  nonstring ->111;  string without    .xml -> abc
#         Happy path
    def test200_010_ShouldReturnSightingFile(self):
        expectedPassName = "dj.xml"
        theFix = Fix.Fix()
        returnedValue = theFix.setSightingFile(expectedPassName)
        self.assertEqual(expectedPassName,returnedValue)
          
    def test200_020_ShouldWriteEntryOfSightingFile(self):
        theFix = Fix.Fix()
        theFix.setSightingFile("sightings.xml")
        theLogFile = open("log.txt",'r')
        entry = theLogFile.readlines()
        self.assertEqual(-1,entry[0].find("Start of sighting file"))
 
#        Sad path
    def test200_020_ShouldRaiseExceptionOnNull(self):
        expectedDiag = self.className + "setSightingFile:  "
        theFix = Fix.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile("")
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)])
                 
    def test200_030_ShouldRaiseExceptionOnMissTitle(self): 
        expectedDiag = self.className + "setSightingFile:  "  
        theFix = Fix.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile(".xml")
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)])
#         
    def test200_040_ShouldRaiseExceptionOnWrongPosition(self):
        expectedDiag = self.className + "setSightingFile:  "
        theFix = Fix.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setSightingFile("aaa.xmlaaa")
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)])
#                 
#                 
# 
# #    Acceptence Test:300
# #        Analysis-getSettings
# #            Inputs 
# #                 no params 
# #            Outputs
# #                 return tuple (approximateLatitude, approximateLongitude)
# #                    a tuple with ('0d0','0d0')
# #            state change:
# #            Navigation Calculation are written into the log file 
# #       
# #         Happy  path 
# #            nominal case for return(0d0.0 , 0d0.0)
# #            nominal case with default log.txt has contents write into the logFile"
# #            nominal case with given logFile for "end of sighting file "be written  into the log file"
# #            nominal case  log are sorted and written in 
# #
# #       Sad path
# #                no sightingFile has been set 
# #                lose mandatory tag in sighting file 
# #                fix not exist 
# #                no sightingFile exist 
# #                sighting   
# #                body missing 
# #                date missing or date not valid format
# #                time  missing  or time not valid format
# #                observation missing 
# #``              observation content is .LT. 0d0.1
# #                observed altitude  is not  LT.0.1 arc-minutes
# #                height content is not numeric 
# #                height content is not G.E.0
# #                invalid information in tag     
# #                a sighting file has more than one "<fix>" tag
# #                temperature content is not an integer 
# #                temperature contents is not in range  G.E.-20  L.E. 120
# #                pressure content is not an integer 
# #                pressure content is an integer , without in the limited  range 
# #
# #
# #       Happy path
    def test300_010_ShouldReturnPredefinedLatLon(self):
        theFix = Fix.Fix()
        theFix.setSightingFile('validOneStarSighting.xml')
        result = theFix.getSightings()
        self.assertTupleEqual(result, ("0d0.0", '0d0.0'))
         
    def test300_620_ShouldExtractOneSightingTag(self):
        theFix = Fix.Fix()
        theFix.setSightingFile('validOneStarSighting.xml')
        result = theFix.getSightings()
        self.assertEqual( 'Aldebaran',result[0])
     
    def test300_630_ShouldRaiseExceptionOnMissingBodyTag(self):
        theFix = Fix.Fix()
        theFix.setSightingFile("noBodySighting.xml")
        with self.assertRaises(ValueError) as context:
            result = theFix.getSightings()
             
    def test300_640_ShouldExtractDateTag(self):
        theFix = Fix.Fix()
        theFix.setSightingFile("validOneStarSighting.xml")
        result = theFix.getSightings()
        self.assertEqual("2016-03-01", result[1])
 
 
    def test300_650_ShouldExtractTimeTag(self):
        theFix = Fix.Fix()
        theFix.setSightingFile("validOneStarSighting.xml")
        result = theFix.getSightings()
        self.assertEqual("23:40:01", result[2])
 
    def test300_660_ShouldExtractObservationTag(self):
        theFix = Fix.Fix()
        theFix.setSightingFile("validOneStarSighting.xml")
        result = theFix.getSightings()
        self.assertEqual("015d04.9", result[3])
 
    def test300_670_ShouldExtractHeightTag(self):
        theFix = Fix.Fix()
        theFix.setSightingFile("validOneStarSighting.xml")
        result = theFix.getSightings()
        self.assertEqual("6.0", result[4])
     
    def test300_680_ShouldExtractDefaultHeightTag(self):
        theFix = Fix.Fix()
        theFix.setSightingFile("noHeightSighting.xml")
        result = theFix.getSightings()
        self.assertEqual("0.0", result[4])
 
    def test300_690_ShouldRaiseExceptionOnInvalidHeight(self):
        theFix = Fix.Fix()
        theFix.setSightingFile("invalidHeightSighting")
        with self.assertRaises(ValueError) as context:
            result = theFix.getSightings()
             
    def test300_700_ShouldExtractPressureTag(self):
        theFix = Fix.Fix()
        theFix.setSightingFile("validOneStarSighting.xml")
        result = theFix.getSightings()
        self.assertEqual("1010", result[5])
 
    def test300_710_ShouldExtractDefaultPressureTag(self):
        theFix = Fix.Fix()
        theFix.setSightingFile("noPressureSighting.xml")
        result = theFix.getSightings()
        self.assertEqual("1010", result[5])
         
    def test300_720_ShouldRaiseExceptionOnInvalidPressure(self):
        theFix = Fix.Fix()
        theFix.setSightingFile("invalidPressure1.xml")
        with self.assertRaises(ValueError) as context:
            result = theFix.getSightings()
        theFix.setSightingFile("invalidPressure2.xml")
        with self.assertRaises(ValueError) as context:
            result = theFix.getSightings()
        theFix.setSightingFile("invalidPressure3.xml")
        with self.assertRaises(ValueError) as context:
            result = theFix.getSightings()



# # Acceptence test400
#    Analysis: setAriesFile
#          inputs:
#            ariesFile:string ,mandatory , unvaidated,  format = f.txt   (len(f)) >=1
#         outputs:
#             return: string with file name   &  absolute file path 
#            write :"Aries file:" &  absolute file path into 
#          file  format:
#            mm/dd/yy \t  hh \t  xdy.y \n
#            mm: 2 digits num  01~12
#            dd: 2 digits num  01~31 depend on month 
#            yy: 2 digits num  00~99
#            hh: 1 or 2 digit num  0~23
#        xdy.y:  x-< 0~360(samne like angle)
#        happyTests:
#            ariesFile:
#                legal file name  -> setAriesFile("ariesFile.txt")
#        sadTests:
#           ariesFile:
#                nonString -> setAriesFile(33)
#                length error -> setAriesFile(".txt")
#                nonTXT -> setAriesFile("ariesFile.xml")
#                missing -> setAriesFile()
#                nonexistent file ->setAriesFile("missing.txt")
    def test400_010_ShouldConstructWithKeyWordParm(self):
        theFix = Fix.Fix()
        try:
            result = theFix.setAriesFile("aries.txt")
            self.assertEquals(result,"aries.txt")
        except:
            self.fail("incorrect keyword specified in setAries parm")
        self.cleanup()


    def test400_020_ShouldRaiseExceptionOnNonStringFileName(self):
        exceptDiag = self.className + "setAriesFile: "
        theFix = Fix.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setAriesFile(123)
        self.assertNotEquals(exceptDiag , context.exception.args[0][0:len(exceptDiag)],"non-string file name")

    def test400_030_ShoulRaiseExceptionOnFileLenError(self):
        exceptDiag = self.className + "setAriesFile: "
        theFix = Fix.Fix()
        with self.assertRaises(ValueError) as context :
            theFix.setAriesFile(".txt")
        self.assertEquals(exceptDiag, context.exception.args[0][0:len(exceptDiag)],"failue for GE.1 aries file name")


    def test400_040_ShouldRaiseExceptionOnMissingFileName(self):
        exceptDiag = self.className + "setAriesFile: "
        theFix = Fix.Fix()
        with self.assertRaises(ValueError) as context :
            theFix.setAriesFile()
        self.assertEquals(exceptDiag, context.exception.args[0][0:len(exceptDiag)],"missing aries file")



#     def test400_050_ShouldRaiseExceptionOnMissingFile(self):
#         exceptDiag = self.className + "setAriesFile: "
#         theFix = Fix.Fix()
#         with self.assertRaises(ValueError) as context:
#             theFix.setAriesFile(self)






# Acceptence test 500
#        Analysis: setStarFile
#            inputs:
#                starFile:string mandatory, unvalidated. format = f.txt  (len(f)>=1)
#       outputs:
#             return: string with file name   &  absolute file path 
#            write :"star file:" &  absolute file path into 
#
###
###         file format 
###            body :string
###            mm / dd/ yy / hh / x / d / y / z 
###
###
#       Happy tests:
#           starFile:
#              legal file name -> setStarFile("starFile.txt")
#       sad tests:
#           starFile:
#               nonString -> setStarFile(11)
#               length error -> setStarFile(".txt")
#               nonTXT -> setStarFile("setStarFile.xml")
#               missing -> setStarFile()
#               nonexistent file -> setStarFile("missing.txt")


    def test500_010_ShouldConstructWithKeyWordParm(self):
        theFix = Fix.Fix()
        try:
            result = theFix.setStarFile("stars.txt")
            self.assertEquals(result,"stars.txt")
        except:
            self.fail("incorrect keyword specified in setStar parm")
        self.cleanup()


    def test500_020_ShouldRaiseExceptionOnNonStringFileName(self):
        exceptDiag = self.className + "setStarsFile: "
        theFix = Fix.Fix()
        with self.assertRaises(ValueError) as context:
            theFix.setStarFile(123)
        self.assertNotEquals(exceptDiag , context.exception.args[0][0:len(exceptDiag)],"non-string file name")

    def test500_030_ShoulRaiseExceptionOnFileLenError(self):
        exceptDiag = self.className + "setStarsFile: "
        theFix = Fix.Fix()
        with self.assertRaises(ValueError) as context :
            theFix.setStarFile(".txt")
        self.assertEquals(exceptDiag, context.exception.args[0][0:len(exceptDiag)],"failue for GE.1 Star file name")


    def test500_040_ShouldRaiseExceptionOnMissingFileName(self):
        exceptDiag = self.className + "setStarsFile: "
        theFix = Fix.Fix()
        with self.assertRaises(ValueError) as context :
            theFix.setStarFile()
        self.assertEquals(exceptDiag, context.exception.args[0][0:len(exceptDiag)],"missing stars file")


# Acceptence test 600
#   Analysis getGHA 
#        happy path: 
#       A: Find angular
#            have to find observed body in star  file for date and observation ;  and use early date 
#               geographic position latitude = star'  declination  om star file
#                    SHA star  =  Sidereal Hour Angle   in star file 
#       B:find GHA of Aries for  date and time 
#            locate the entry for GHA of 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 


