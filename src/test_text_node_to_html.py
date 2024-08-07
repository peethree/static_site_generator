import unittest

from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode
from htmlnode import LeafNode

class TestNodeToHTML(unittest.TestCase):
    def test_text_node_to_html_node_text(self):
        node = TextNode("This is a text node", "text", "https://www.boot.dev")
        result = text_node_to_html_node(node)
        self.assertEqual(result, LeafNode("This is a text node", None, None))
        

    def test_text_node_to_html_node_bold(self):
        node = TextNode("Test", "bold", None)
        result = text_node_to_html_node(node)
        self.assertEqual(result, LeafNode("b", "Test", None))

    def test_text_node_to_html_node_italic(self):
        node = TextNode("testing", "italic", None)
        result = text_node_to_html_node(node)
        self.assertEqual(result, LeafNode("i", "testing", None))

    def test_text_node_to_html_node_code(self):
        node = TextNode("T-t-test", "code", None)
        result = text_node_to_html_node(node)
        self.assertEqual(result, LeafNode("code", "T-t-test", None))
        

    def test_text_node_to_html_node_line(self):
        node = TextNode("Test", "link", "https://myfavwebsite.com")
        result = text_node_to_html_node(node)              
        self.assertEqual(result, LeafNode("a", "Test", {"href": "https://myfavwebsite.com"}))

    def test_text_node_to_html_node_image(self):
        node = TextNode("test123", "image", "googoo.com")
        result = text_node_to_html_node(node)               
        self.assertEqual(result, LeafNode("img", "", {"src": "googoo.com", "alt": "test123"}))



    def test_raise_exception(self):
        # If it gets a TextNode that is none of those types, it should raise an exception.        
        with self.assertRaises(Exception) as context:
            node = TextNode("TeST", "invalid type", None)
            text_node_to_html_node(node)

            self.assertEqual(str(context.exception), "Invalid text type")

