from piece import Piece


class Cube:
    def __init__(self, lo, hi):
        self.pieces = []
        self.scramble = []
        self.generate_cube(lo, hi)

    # Creates a 3x3 array of piece objects
    def generate_cube(self, lo, hi):
        for x in range(lo, hi):
            for y in range(lo, hi):
                for z in range(lo, hi):
                    self.pieces.append(Piece(x, y, z))

    def get_cube(self):
        return self.pieces

    # Rotates all cubes on the x axis
    def turn_x(self, layer, direction):
        for qb in self.pieces:
            if qb.get_location()[0] == layer:
                qb.rotate_x(direction)

    def turn_y(self, layer, direction):
        for qb in self.pieces:
            if qb.get_location()[1] == layer:
                qb.rotate_y(direction)

    def turn_z(self, layer, direction):
        for qb in self.pieces:
            if qb.get_location()[2] == layer:
                qb.rotate_z(direction)

    # adds array of moves to scramble
    def add_moves(self, moves):
        self.scramble.extend(moves)

    # returns last move in scramble
    def get_scramble(self):
        if len(self.scramble) == 0:
            return None
        return self.scramble.pop()

    # draws each piece in cube
    def show(self):
        for qb in self.pieces:
            qb.draw()

