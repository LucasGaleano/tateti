#! /usr/bin/env python3
from table import Table
from player import Player
from move import *


def equals(expresion, result):
    return expresion == result


table = Table([['X',' ',' '],[' ',' ',' '],[' ',' ',' ']])

print('test table')
print(equals(table.findFirstPositionFree(), 2))

table2 = Table([[' ',' ','X'],[' ',' ',' '],[' ',' ',' ']])
print(equals(table2.findFirstPositionFree(), 1))
