import unittest

from htmlnode import ParentNode
from htmlnode import LeafNode

class TestParentNode(unittest.TestCase):

    # test if no tag raises value error
    def test_parent_node_tag(self):
        
        with self.assertRaises(ValueError) as context:
            
            child = LeafNode("a", "test", None)
            node = ParentNode(None, child, {"href": "https://www.google.com"}) 
            node.to_html()                 
        
        self.assertEqual(str(context.exception), "ParentNode needs a tag")

    # parent (text) value is none
    def test_parent_node_value(self):
        child = LeafNode("a", "test", None)
        node = ParentNode("a", child, None)

        self.assertIsNone(node.value)

    # test if no children raises error
    def test_parent_node_child(self):
        with self.assertRaises(ValueError) as context:            
            
            node = ParentNode("p", None, None) 
            node.to_html()                 
        
        self.assertEqual(str(context.exception), "ParentNode needs to have a child")

    # test if html is parsed correctly in parent node class
    def test_parent_to_html(self):

        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        result = node.to_html()
        self.assertEqual(result, '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')
