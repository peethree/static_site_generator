import unittest

from split_nodes import split_nodes_image, split_nodes_link
from textnode import TextNode

class TestSplitNodes(unittest.TestCase):
    def test_split_image(self):
        nodes = [TextNode("This is text with an image of ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
        "text"), TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", "text")
        ]
        result = split_nodes_image(nodes)

        self.assertEqual(result, [TextNode("This is text with an image of ", "text"), 
                                  TextNode("to boot dev", "image", "https://www.boot.dev"), 
                                  TextNode(" and ", "text"), 
                                  TextNode("to youtube", "image", "https://www.youtube.com/@bootdotdev"), 
                                  TextNode("This is text with a ", "text"), 
                                  TextNode("rick roll", "image", "https://i.imgur.com/aKaOqIh.gif"), 
                                  TextNode(" and ", "text"), 
                                  TextNode("obi wan", "image", "https://i.imgur.com/fJRm4Vk.jpeg")])


    def test_split_link(self):
        nodes = [TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        "text")]
        result = split_nodes_link(nodes)

        self.assertEqual(result, [TextNode("This is text with a link ", "text"), 
                                  TextNode("to boot dev", "link", "https://www.boot.dev"), 
                                  TextNode(" and ", "text"), 
                                  TextNode("to youtube", "link", "https://www.youtube.com/@bootdotdev")])
        
    def test_split_node_image_no_images(self):
         nodes = [TextNode("This is text without an image", "text")]
         result = split_nodes_image(nodes)

         self.assertEqual(result, [TextNode("This is text without an image", "text")])

        
    def test_split_node_link_no_links(self):
        nodes = [TextNode("This is text without an image", "text")]
        result = split_nodes_link(nodes)

        self.assertEqual(result, [TextNode("This is text without an image", "text")])


        # +  TextNode(obi wan, image, https://i.imgur.com/fJRm4Vk.jpeg)]