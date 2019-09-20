#! /usr/bin/env python3
from table import Table
from player import Player
from move import *


def equals(expresion, result):
    return str(expresion == result)

print('------------')
print('test table')
table = Table([['X',' ',' '],[' ',' ',' '],[' ',' ',' ']])
print('elige la segunda posicion: ' + equals(table.findFirstPositionFree(), 2))

table = Table([[' ',' ','X'],[' ',' ',' '],[' ',' ',' ']])
print('elige la primera posicion: ' + equals(table.findFirstPositionFree(), 1))

table = Table([['O','O','X'],[' ','X',' '],[' ',' ',' ']])
print('elige la cuarta posicion: ' + equals(table.findFirstPositionFree(), 4))

print('------------')
print('test winner')
table = Table([['O','O','X'],[' ','X',' '],['O',' ',' ']])
print('Sin ganador: ' + equals(table.checkWinner(), None))

table = Table([['O','O','O'],[' ','X',' '],['O',' ',' ']])
print('ganador la O fila: ' + equals(table.checkWinner(), 'O'))

table = Table([['O','X','X'],['O','X',' '],[' ','X',' ']])
print('ganador la X diagonal: ' + equals(table.checkWinner(), 'X'))
