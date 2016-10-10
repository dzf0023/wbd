class Angle():
 
    def __init__(self):
        self.angle = 0.0
        self.className = "Angle."
        
    
    
    
    def setDegrees(self,degrees=0):
        methodName = "setDegrees:  "
        if (not(isinstance(degrees,(int,float)))):
            raise ValueError(self.className + methodName + "invalid value") 
        self.angle = self.calculateAngle(degrees)
        return self.angle  
        
        
  
       
    def setDegreesAndMinutes(self,degrees=None):
        methodName = "setDegreeAndMinutes:  "
        if(not(isinstance(degrees,int))) | (degrees = None):
            raise ValueError(self.className + methodName + "invalid value")
        if(not(isinstance(minutes,))) | (minutes< 0):
            raise ValueError(self.className + methodName + "invalid value")
        try:
            findOfDivid = degrees.find('d')  
                if(findOfDivid == 0) | (findOfDivid == -1):
                    raise ValueError
                
        degreePart = int(degrees[0:findOfDivid]) 
        minutePart = degrees[findOfDivid+1:len(degrees)]
        if("-" in minutePart):
            raise ValueError
        decimalPoint = minutePart.find(".")
        if(decimalPoint != -1):
            if((decimalPoint == 0) or (len(minutePart)-decimalPoint > 2)):
                raise ValueError
            
            if degreePart >= 0.0:
                self.angle = float((degreePart%360.0 + minutePart/60.0)%360.0)
            elif degreePart < 0.0 and (degreePart%360 - minutePart/60.0) > 0.0:
                self.angle = float (degreePart%360 - minutePart/60.0) 
            elif degreePart < 0.0 and (degreePart%360 - minutePart/60.0) <0.0:
                self.angle = float (degreePart%360 - minutePart/60.0 + 360.0)
        
        except ValueError:
            raise ValueError(self.className + methodName + "invalid value")
        
        return self.angle       





    def add(self,angle=None):
        methodName = "add:  "
        if(not(isinstance(angle, Angle))) | (angle == None):
            raise ValueError(self.className + methodName + "invalid value") 
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


    def calculateAngle(self,angle):
        #methodName = "calculateAngle:"
        if  0 <= float(angle) < 360: 
            angle = float(angle)
        else:
            angle = float(angle)%360
        return angle
    
    
    
    