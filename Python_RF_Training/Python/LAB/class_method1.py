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

class Date(object):
    day = 0
    month = 0
    year = 0
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year
        print "Date %d Month %d Year %d" %(day, month, year)

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

if __name__ == '__main__':
    date2 = Date.from_string('11-09-2012')
    print date2