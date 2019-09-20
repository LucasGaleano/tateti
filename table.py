
import os
import math

class Table():

    table = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    def __init__(self, table = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]):
        self.table = table


    def start():
        self.nextMove()
        self.refresh()

    def turn(self, player):
        self.refresh()
        player.move(self)
        #self.checkWinner()

    def print(self):
        for i in range(3):
            print(str(self.table[i][0]) + '|' + str(self.table[i][1]) + '|' + str(self.table[i][2]))

    def printWinner(self):
        table.refresh()
        print('Winner: ' + self.checkWinner())

    def refresh(self):
        os.system('reset')
        self.print()

    def fill(self,blockNumber, character):
        self.table[self.row(blockNumber)][self.column(blockNumber)] = character

    def column(self, number):
        return math.floor((number%3)-1)

    def row(self, number):
        return math.floor((number-1)/3)

    def findFirstPositionFree(self):
         for i in range(3):
             if ' ' in self.table[i]:
                return (i+1)*3-(2-self.table[i].index(' '))

    def checkWinner(self):
        for i in range(3):
            if self.checkColumn(i):
                if self.table[i][0] == ' ':
                    return None
                return self.table[i][0]

            if self.checkRow(i):
                if self.table[0][i] == ' ':
                    return None
                return self.table[0][i]

    def checkColumn(self, column):
        return self.table[column][0]== self.table[column][1] and self.table[column][1] == self.table[column][2]

    def checkRow(self, row):
        return self.table[0][row]== self.table[1][row] and self.table[1][row] == self.table[2][row]
