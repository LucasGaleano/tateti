
import os
import math
import random

class Table():

    def __init__(self, table = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]):
        self.table = table

    def start(self, players):
        random.shuffle(players)
        iter_players = self.players(players)
        while True:
            self.turn(next(iter_players))
            if(self.checkWinner()):
                break
        self.printWinner()


    def turn(self, player):
        self.refresh()
        player.move(self)

    def print(self):
        print()
        for i in sorted(range(3),reverse=True):
            print(str(self.table[i][0]) + '|' + str(self.table[i][1]) + '|' + str(self.table[i][2]))

    def printWinner(self):
        self.refresh()
        print('Winner: ' + self.checkWinner())

    def refresh(self):
        os.system('reset')
        self.print()

    def fill(self, position, character):
        self.table[self.row(position)][self.column(position)] = character

    def column(self, number):
        return math.floor((number%3)-1)

    def row(self, number):
        return math.floor((number-1)/3)

    def findFirstPositionFree(self):
         for i in range(3):
             if ' ' in self.table[i]:
                return (i+1)*3-(2-self.table[i].index(' '))

    # TODO terrible arbol de ifs jajaja despues refactorizo
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

            if self.checkDiagonal():
                if self.table[1][1] == ' ':
                    return None
                return self.table[1][1]

    def checkColumn(self, column):
        return self.table[column][0]== self.table[column][1] and self.table[column][1] == self.table[column][2]

    def checkRow(self, row):
        return self.table[0][row] == self.table[1][row] and self.table[1][row] == self.table[2][row]

    def checkDiagonal(self):
        return (self.table[0][0] == self.table[1][1] and self.table[1][1] == self.table[2][2]) or (self.table[2][0] == self.table[1][1] and self.table[1][1] == self.table[0][2])

    def players(self, players):
        while True:
            for player in players:
                yield player
