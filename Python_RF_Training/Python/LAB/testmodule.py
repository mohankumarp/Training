#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MohanKumarP
#
# Created:     19/12/2015
# Copyright:   (c) MohanKumarP 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import num

def main():
    pass

x = 2
def f(a):
    #global x
    print x
    x = a * a
    return x



if __name__ == '__main__':
    num.square(3)
    num.cube(3)

    print x
    y = f(3)
    print x, y
