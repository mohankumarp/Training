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

class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")

class C(A):
    def m(self):
        print("m of C called")

class D(B,C):
    def m(self):
        print("m of D called")
        B.m(self)
        C.m(self)
        A.m(self)

if __name__ == '__main__':
    from multiple_inheritence3 import D
    x = D()
    x.m()



