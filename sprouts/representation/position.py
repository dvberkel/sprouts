class Representation:
    @staticmethod
    def of(representation):
        return Position(representation)

class Position:
    def __init__(self, representation):
        self.representation = representation

    def removeDeadParts(self):
        return Position(self.representation)

    def __eq__(self, other):
        return self.representation == other.representation

    def __hash__(self):
        return hash(self.representation)
