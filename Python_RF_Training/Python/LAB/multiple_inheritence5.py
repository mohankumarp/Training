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
    def _m(self):
        print("m of B called")
    def m(self):
        self._m()
        A.m(self)

class C(A):
    def _m(self):
        print("m of C called")
    def m(self):
        self._m()
        A.m(self)

class D(B,C):
    def m(self):
        print("m of D called")
        B._m(self)
        C._m(self)
        A.m(self)

if __name__ == '__main__':
    from multiple_inheritence5 import D
    x = D()
    x.m()