import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_text_type(self):
        node = TextNode("also a test", "italic")
        node2 = TextNode("also a test", "bold")
        self.assertNotEqual(node, node2)       

    def test_text(self):
        node = TextNode("aaaa", "bold")
        node2 = TextNode("bbbb", "bold") 
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("a", "b")        
        self.assertIsNone(node.url)

# Add even more tests (at least 3 in total) to check various edge cases, 
# like when the url property is None, or when the text_type property is different. 
# You'll want to make sure that when properties are different, 
# the TextNode objects are not equal.



if __name__ == "__main__":
    unittest.main()