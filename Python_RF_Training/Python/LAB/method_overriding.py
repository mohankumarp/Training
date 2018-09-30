#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MohanKumarP
#
# Created:     20/12/2015
# Copyright:   (c) MohanKumarP 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Base(): # Base class
##    def add(self,a,b):
##        s = a + b
##        print "Base class Add with 2 args: ", s

    def add(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

        sum = a + b + c
        print "Base class Add with 3 args: ", sum

class Derived(Base): # Derived class
    def add(self,a,b): # overriding method
        sum = a + b
        print "Derived class Add with 2 args: ",  sum

if __name__ == '__main__':
    base=Base() #instance creation for Base class
    derived=Derived()#instance creation for Derived class

    base.add(4,2,5) # function with 3 arguments
    #base.add(4,2) # function overloading not supported in base class
    #derived.add(4,2,5) # function overloading not supported in derived class
    derived.add(4,2)   # function with 2 arguments overrides base clas 'add(self,a,b,c)' function

