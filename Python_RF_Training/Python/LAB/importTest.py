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
#import num as number           #option-1
import importlib
number = importlib.import_module('num')    #option-2

def import_from(module, name):
    module = __import__(module, fromlist=[name])
    return getattr(module, name)

def main():
    pass

if __name__ == '__main__':

    print number.square(3)
    print number.cube(3)
    print number.__name__
    print number.__file__
    print number.__package__

    #sqr = import_from('num', 'square')         #option-2
    #print sqr(3)