import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_to_html_node import text_to_children
from text_to_textnodes import text_to_textnodes

# class TestTextToChildren(unittest.TestCase):

#     def test_text_to_children(self):
#         pass
#         text = "**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)"
#         text_nodes = text_to_textnodes(text)
#         # result = text_to_children(text_nodes)

#         self.assertEqual(text_nodes, "[TextNode(I like Tolkien, bold, None), TextNode(. Read my , text, None), TextNode(first post here, link, /majesty), TextNode( (sorry the link doesn't work yet), text, None)]")