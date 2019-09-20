import time

def move_manual(table):
    print()
    print('Enter play 1-9: ')
    return int(input())

def move_easyAI(table):
    print()
    print('thinking....')
    time.sleep(1)
    return table.findFirstPositionFree()
