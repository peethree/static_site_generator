import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)


    # text_type property is different
    def test_text_type(self):
        node = TextNode("also a test", "italic")
        node2 = TextNode("also a test", "bold")
        self.assertNotEqual(node, node2)       

    # text not equal
    def test_text(self):
        node = TextNode("aaaa", "bold")
        node2 = TextNode("bbbb", "bold") 
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("a", "b")        
        self.assertIsNone(node.url)



if __name__ == "__main__":
    unittest.main()