import Navigation.prod.Angle as Angle

angle1 = Angle.Angle()
angle2 = Angle.Angle()
angle3 = Angle.Angle()

def setDegrees(degrees):
    if (not(isinstance(degrees,(int,float)))):
        raise ValueError("degrees should be int or float") 
    if  0 <= degrees <= 360: 
        return degrees
    else:
        R =  degrees%360
        return R   
#returnValue = setDegrees(input())
#print returnValue



def __init__(self,angle):
    self.angle = angle
    return angle




def add(angle,angle1):
        angle1 = float(input())
        angle = float(input())
        angle1 = angle + angle1
        if(not(isinstance(angle1,float))):
            raise ValueError("angle should be a floating number")
        if  0 <= angle1 <= 360: 
            return angle1
        else:
            angle1 =  angle1%360
        return angle1
    
#returnValue = add(input())   
#print returnValue 
    
    
    
    
def setDegreesAndMinutes(self, degrees,minutes):
        self.degrees = int(input())
        self.minutes = float(input())
        if(not(isinstance(degrees, int))):
            raise ValueError("degrees shoule be int")
        if(not(isinstance(minutes(int,float)))):
            raise ValueError("minutes shoule be int or float")
        x = degrees 
        y = minutes
        return str(x)+'d'+str(y)


returnValue = setDegreesAndMinutes.input()
print returnValue
    