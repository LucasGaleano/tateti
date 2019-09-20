import time

def move_manual(table):
    print('Enter play 1-9: ')
    return int(input())

def move_easyAI(table):
    print('thinking....')
    time.sleep(1)
    return table.findFirstPositionFree()
