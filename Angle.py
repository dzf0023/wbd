class Angle():
 
    def __init__(self):
        self.angle = 0.0
        self.className = "Angle."
        
    
    def calculateAngle(self,angle):
        angle = float(angle)%360
        return angle
    
    
    def setDegrees(self,degrees=0):
        methodName = "setDegrees:  "
        if (not(isinstance(degrees,(int,float)))):
            raise ValueError(self.className + methodName + "invalid value") 
        self.angle = self.calculateAngle(degrees)
        return self.angle  
        
        
  
       
    def setDegreesAndMinutes(self,degrees=None):
        methodName = "setDegreesAndMinutes: "
        angle = 0.0
        if(not(isinstance(degrees, str))):
            raise ValueError(self.className + methodName + "informal")
        if (degrees == 0 or degrees == None):
            raise ValueError(self.className + methodName + "not exist degrees ")
        try:
            findOfDivid = degrees.index("d")  
            if(findOfDivid == 0):
                raise ValueError(self.className + methodName + "wrong position ")            
            degreePart = int(degrees[0:findOfDivid])
            if (not(isinstance(degreePart, int))):
                raise ValueError(self.className + methodName +" Degree should be integer ")
                
            minutePart = degrees[findOfDivid+1:len(degrees)]
            float(minutePart)
#             if (not(isinstance(minutePart, int)) or not(isinstance(minutePart, float))):
#                 raise ValueError(self.className + methodName +" Minute should be integer or float  ")
#             if (minutePart<0.0):
#                 raise ValueError(self.className + methodName + "minutePart should positive")
            findOfMinus = minutePart.find("-")
            if(findOfMinus != -1):
                raise ValueError(self.className + methodName + "minutePart should positive")
        
            decimalPoint = minutePart.find(".")
            
            if(decimalPoint!= -1):
                if not minutePart[-2]==".":
                    raise ValueError(self.className + methodName +"Bad decimal place!")
#                 if((len(minutePart)-decimalPoint > 2) or (decimalPoint ==0)):
#                     raise ValueError(self.className + methodName +"wrong Decimal")
        
            minutePortion = float(minutePart) / 60.0
            if(-360.0 < degreePart  < 0):
                angle = 360.0-( 360-(degreePart%360) + minutePortion)
            else:
                angle = degreePart % 360.0 + minutePortion
        except:
            raise ValueError(self.className + methodName + "invalid111 ")
        self.angle = self.calculateAngle(angle)
        return angle
        
     
        
        
    def add(self,angle=None):
        methodName = "add:  "
        if(not(isinstance(angle, Angle))) | (angle == None):
            raise ValueError(self.className + methodName + "add problem") 
        try: 
            self.angle+=angle.getDegrees()  
            self.angle=self.calculateAngle(self.angle)
 
        except:
            raise ValueError("something wrong")
        return self.angle
       
     
    def subtract(self, angle=None):
        methodName = "subtract:  "
        if(not(isinstance(angle,Angle))) | (angle == None):
            raise ValueError(self.className + methodName + "invalid value") 
        try: 
            self.angle =self.angle-angle.getDegrees()  
            self.angle = self.calculateAngle(self.angle)
        except:
            raise ValueError("invalid value") 
        return self.angle        
       
    
    
    
    
    def compare(self, angle=None):
        methodName = "compare:  "
        if(not(isinstance(angle,Angle))) | (angle == None):
            raise ValueError(self.className + methodName + "invalid value") 
        if (self.angle > angle.getDegrees()):
            return 1
        elif (self.angle < angle.getDegrees()):
            return -1
        else:
            return 0

    def getString(self):
        #methodName = "getString:"
        link = self.getDegrees()
        self.start = int(link)
        self.end = round((link - self.start)*60,1)
        entireString = str(self.start)+'d'+str(self.end)
        return entireString            
    


    def getDegrees(self):
        #methodName = "getDegrees:"
        temp = self.angle
        degree= int(temp)
        if(degree == 0):
            Minute = temp
        else:
            Minute = temp % degree
        roundedMinute = round(Minute*60,1)/60
        temp = degree + roundedMinute
        return temp


    
    
    
    