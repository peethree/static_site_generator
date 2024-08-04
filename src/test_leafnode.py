import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):       
        node = LeafNode("p", "This is a paragraph of text.")   
        result = node.to_html()  
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        result2 = node2.to_html()
        self.assertEqual(result, "<p>This is a paragraph of text.</p>")
        self.assertEqual(result2, '<a href="https://www.google.com">Click me!</a>')

    def test_if_no_children(self):
        child = LeafNode("a", "test", None)
        node = LeafNode("p", "double test", child)
        self.assertIsNone(node.children)

    def test_no_value_to_html(self):
        with self.assertRaises(ValueError) as context:
            # leafnode with value of none should raise ValueError
            node = LeafNode("p", None, None)
            result = node.to_html()        
        
        self.assertEqual(str(context.exception), "All leaf nodes must have a value")

