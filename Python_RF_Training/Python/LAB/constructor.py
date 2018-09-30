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

class TestClass:

    def __init__(self):
        print ("constructor")

    def __del__(self):
        print ("destructor")

if __name__ == "__main__":
    obj = TestClass()
    del obj

