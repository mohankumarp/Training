import os
#import os
import sys
from subprocess import Popen, call,CalledProcessError,check_call
from tempfile import TemporaryFile

#1.computing area of circle
class  Workspace1():
   """Python programs for exercise1"""
    def _init_(self,value):
    self.value=value
   def area(self,radius):
    area=3.14*(radius**2)
    return area
   def area2(self):
    arg=int(raw_input("Enter the value of radius :"))
    area=3.14*(arg**2) 
    return area
   def conversion(self):
    arg=float(raw_input("Enter the value of dollar:"))
    rupee=arg/50
    return rupee
   def stringreverse(self):
    arg=raw_input("Enter a string :")
    revstring=list(arg)
    str1=arg[::-1]
    print "Reverse of given string is :%s",str1
    for i in range(1,len(revstring)):
      print revstring[-i]
   def getfileext(self,arg):
    #print os.path.dirname(__file__)
    print os.path.dirname(__file__)
    extension = os.path.splitext(arg)[1]
    print extension
   def ntimesx(self,arg):
    str1=""
    for i in range(0,arg):
     str1=str1+"X"
    for j in range(0,arg):
     print str1
    #return str1
a=Workspace1()
print a.getfileext("D:\My Documents\Desktop\pythonexercises\sample.txt")