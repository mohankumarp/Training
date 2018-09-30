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
    def showMSG(self):
        print 'first method'
    def showMSG(self, i):
        print 'second method ', i



def main():
    pass

if __name__ == '__main__':
    ob = A()
    ob.showMSG(2)
    #ob.showMSG()
    main()
