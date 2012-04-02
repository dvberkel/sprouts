import unittest

from sprouts.representation.position import Representation

class testRepresentation(unittest.TestCase):
    def testCreationOfRepresentation(self):
        self.assertNotEqual(None, Representation.of("A.B.C.}!"))

if __name__ == '__main__':
    unittest.main()
