class Angle:
 
    
    def __init__(self,angle):
        self.angle = angle
        return angle 
        
    
    
    
    def setDegrees(self,degrees):
        if (not(isinstance(degrees,(int,float)))):
            raise ValueError("degrees should be int or float") 
        if  0 <= degrees <= 360: 
            return degrees
        else:
            R =  degrees%360
            return R  
        
        
  
       
    def setDegreesAndMinutes(self,degrees,minutes):
        self.degrees = degrees
        self.minutes = minutes
    
        degrees = int(input("degrees: "))

        if not isinstance(degrees,int):
            raise ValueError("degrees should be int")

        minutes = float(input("minutes: "))

        if not isinstance(minutes,(int,float)): 
            raise ValueError("minutes should be int or float")
        #f = setDegreesAndMinutes()
        print(str(f.degrees)+ 'd' + str(f.minutes))
    
    
    
    
    def add(self, angle,angle1):
        angle1 = angle + angle1
        if(not(isinstance(angle1,float))):
            raise ValueError("angle should be a floating number")
        if  0 <= angle1 <= 360: 
            return angle1
        else:
            angle1 =  angle1%360
        return angle1
    
    
    
     
    def sub(self, angle,angle1):
        angle1 = angle - angle1
        if(not(isinstance(angle1,float))):
            raise ValueError("angle should be floating number")
        if  0 <= angle1 <= 360: 
            return angle1
        else:
            angle1 =  angle1%360
        return angle1
    
    
    
    
    def compare(self, angle1,angle2):
        self.angle1 = angle1
        self.angle2 = angle2
        if not isinstance((angle1,angle2),int):
            raise ValueError("degrees should be int")
        
        if angle1 > angle2:
            print'1'
        elif angle1 < angle2:
            print'-1'
        else:
            print'0'
        return
            
       
    
    
    def getString(self,degrees,minutes):
        self.degrees = input(int("degrees"))
        self.minutes = input(float("minutes"))
        minutes  = minutes*60
        print(str(degrees)+ 'd' + str(minutes))
        return
    
        
        
            
    
    def getDegrees(self,degrees):
        self.degrees = degrees
        return(degrees)
    