

class Movable:
    def __init__(self, parts, hitboxPart, hitboxRadius = 20):
        self.parts = parts
        self.hitboxPart = hitboxPart
        self.hitboxRadius = hitboxRadius

    def left(self):
        for ppart in self.parts:
            ppart.left_function()

    def right(self):
        for ppart in self.parts:
            ppart.right_function()

    def down(self):
        for ppart in self.parts:
            ppart.down_function()