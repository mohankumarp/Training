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

if __name__ == '__main__':
    from multiple_inheritence2 import A,B,C,D
    x = D()
    B.m(x)  #m of B called
    C.m(x)  #m of C called
    A.m(x)  #m of A called

