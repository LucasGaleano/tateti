class Player():

    def __init__(self, typeMove, character):
        self.typeMove = typeMove
        self.character = character

    def move(self, table):
        position = self.typeMove(table)
        table.fill(position,self.character)
