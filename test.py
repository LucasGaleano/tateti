#! /usr/bin/env python3
from table import Table
from player import Player
from move import *


def equals(expresion, result):
    return expresion == result

print('test table')
table = Table([['X',' ',' '],[' ',' ',' '],[' ',' ',' ']])
print(equals(table.findFirstPositionFree(), 2))

table = Table([[' ',' ','X'],[' ',' ',' '],[' ',' ',' ']])
print(equals(table.findFirstPositionFree(), 1))

table = Table([['O','O','X'],[' ','X',' '],[' ',' ',' ']])
print(equals(table.findFirstPositionFree(), 4))
