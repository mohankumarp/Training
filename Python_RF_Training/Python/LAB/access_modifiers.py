#-------------------------------------------------------------------------------
# Name:        access_modifiers
# Purpose:
#
# Author:      MohanKumarP
#
# Created:     20/12/2015
# Copyright:   (c) MohanKumarP 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Cup:
    def __init__(self):
        self.shape = "round"
        self.__color = "green"
        self._content = None

    def fill(self, beverage):
        self._content = beverage

    def empty(self):
        self._content = None

    def dispence(self):
        print "shape of cup: ", self.shape
        print "content of cup: ", self._content
        print  "color of cup: ", self.__color

class Mug(Cup):

    def dispence(self):
        print "Derived shape of cup: ", self.shape
        print "Derived content of cup: ", self._content
        print  "color of cup: ", self.__color #Not Accessible


if __name__ == '__main__':
    redCup = Cup()

    redCup.shape = "oval"
    redCup.__color = "red"
    redCup. _content = "tea"
    redCup.dispence()

    redCup.shape = "square"
    redCup.__color = "yellow"
    redCup.empty()
    redCup.fill("coffee")
    redCup.dispence()

    redMug = Mug()
    redMug.fill("greenTea")
    redMug.dispence()
    #print redMug.__color #Error