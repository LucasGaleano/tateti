
import os
import math

class Table():

    table = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]


    def start():
        self.refresh()
        self.nextMove()

    def print(self):
        for i in range(3):
            print(str(self.table[i][0]) + '|' + str(self.table[i][1]) + '|' + str(self.table[i][2]))

    def refresh(self):
        os.system('reset')
        self.print()

    def fill(self,blockNumber, character):
        self.table[self.row(blockNumber)][self.column(blockNumber)] = character

    def column(self, number):
        return math.floor((number%3)-1)

    def row(self, number):
        return math.floor((number-1)/3)

    def findFirstPositionFree():
         for i in range(3):
             if (table[i].index(' '))
                return table[i].index(' ') * (i+1)
