# minutePart=("33d19.3")
# decimalPoint = minutePart.find(".")
# if(len(minutePart)-decimalPoint > 2):
#     raise ValueError("invalid minutePart")
# print decimalPoint
# degrees = ("0d0")
# # findOfDivid = degrees.index('d')  
# # if(findOfDivid == 0):
# #     raise ValueError("wrong position ")
# # degreePart = int(degrees[0:findOfDivid])
# # if degreePart > 3.3:
# #     print "111"
# # minutePart = round(float(degrees[findOfDivid+1:len(degrees)]),1)
# # print findOfDivid
# # print degreePart
# # print minutePart
# # print degreePart*10
# if(degrees ==0):
#     print "222"
# if(degrees != 0):
#     print "1111"
# degrees = "33d-43.2"
# findOfDivid = degrees.index("d") 
# minutePart = float(degrees[findOfDivid+1:len(degrees)])
# if(minutePart < 0):
#     print 
# from datetime import date

#    if not len(sighting.getElementsByTagName("height")[0].childNodes) == 0:


# import xml.dom.minidom as DOM
# dom = DOM.parse("sightings.xml")
# a = dom.getElementsByTagName("time")[0].childNodes[0].data
# print a 


# from time import  strftime,gmtime
# from datetime import date, datetime
# dateTime= strftime("%Y-%m-%d %H:%M:%S")
# dateTime1 =strftime("%Y-%m-%d %H:%M:%S", gmtime())
# # print  dateTime
# from xml.dom import minidom
# dom = minidom.parse('sightings.xml')
# body0 = dom.getElementsByTagName("body")[0].childNodes[0].data
# date0 = dom.getElementsByTagName("date")[0].childNodes[0].data
# time0 = dom.getElementsByTagName("time")[0].childNodes[0].data
# observation0 = dom.getElementsByTagName("observation")[0].childNodes[0].data
# body1 = dom.getElementsByTagName("body")[1].childNodes[0].data
# date1 = dom.getElementsByTagName("date")[1].childNodes[0].data
# time1 = dom.getElementsByTagName("time")[1].childNodes[0].data
# observation1 = dom.getElementsByTagName("observation")[1].childNodes[0].data
# print "LOG:\t"+dateTime+"\tStart of log\n"
# print "LOG:\t"+dateTime +  body0 + date0 +time0 +  observation0

# body = dom.getElementsByTagName("body")[1]
# #date = dom.getElementsByTagName("date")[]
# #time = dom.getElementsByTagName("time")[0]
# #observation = dom.getElementsByTagName("observation")[0]
# print body.firstChild.data