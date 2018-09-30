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

class A(object):
    def print_it(self):
        print 'A'

class B(A):
   def print_it(self):
        print 'B'

if __name__ == '__main__':
    x = B()
    x.print_it()                # calls derived class method as expected

    super(B, x).print_it()      # calls base class method

