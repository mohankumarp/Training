#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MohanKumarP
#
# Created:     22/12/2015
# Copyright:   (c) MohanKumarP 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class A(object):
    def obj_method(self,x):
        print "executing obj_method(%s,%s)"%(self,x)

    @classmethod
    def class_method(cls,x):
        print "executing class_method(%s,%s)"%(cls,x)

    @staticmethod
    def static_method(x):
        print "executing static_method(%s)"%x

if __name__ == '__main__':
    a = A()
    #A.obj_method(20)
    a.obj_method(10)

    a.class_method(10)
    A.class_method(10)

    a.static_method(10)
    A.static_method(10)
