import unittest
from gencontent import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title():

        markdown= "Hello World"
        self.assertEqual(extract_title(markdown),"Hello World")


    def test_extract_title_with_h1():


        markdown= "# Hello World  "
        self.assertEqual(extract_title(markdown), "Hello World")























if __name__ == "__main__":
    unittest.main()