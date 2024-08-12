import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n"
        result = extract_title(markdown)
        self.assertEqual(result, "This is a heading")

    def test_raise_error(self):        
        with self.assertRaises(Exception) as context:
            markdown = "## This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n"
            extract_title(markdown)

        self.assertEqual(str(context.exception), "no title found")


       