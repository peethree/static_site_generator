import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_node_tag(self):
        node = HTMLNode("p", None, None, None)        
        self.assertIsNotNone(node.tag)

    def test_node_text(self):
        node = HTMLNode(None, "AAAaaaa", None, None)
        self.assertIsNotNone(node.value)
    
    def test_node_children(self):
        child = HTMLNode("p", "bbb", None, None)
        node = HTMLNode(None, None, child, None)
        self.assertIsNotNone(node.children)

    def test_node_props(self):
        prop = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode("a", "cccc", None, prop)
        self.assertIsNotNone(node.props)


#node = HTMLNode("p", "text inside a paragraph", None, {"href": "https://www.google.com", "target": "_blank"})
#child = HTMLNode("a", "text", None, {"href": "https://www.google.com", "target": "_blank"})