import pygame
from data.classes.Square import Square
# Game state checker
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tile_width = width // 20
        self.tile_height = height // 20
        self.selected_piece = None
        self.turn = 'white'
        self.squares = self.generate_squares()

    def generate_squares(self):
        output = []
        for y in range(20):
            for x in range(20):
                output.append(
                    Square(x,  y, self.tile_width, self.tile_height)
                )
        return output