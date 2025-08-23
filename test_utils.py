import unittest
import utils

class TestUtils(unittest.TestCase):

    def testConvertToLower(self):
        self.assertEqual("abcdef",utils.slugify("AbCDEf"))
    
    def testCollapseSpaces(self):
        self.assertEqual("abc-def",utils.slugify("AbC DEf"))
    
    def testStripInvalidCharacters(self):
         self.assertEqual("abc-def",utils.slugify("AbC@! DEf@"))


if __name__ == "__main__":
    unittest.main()