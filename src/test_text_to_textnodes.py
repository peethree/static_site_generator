import unittest

from textnode import TextNode
from text_to_textnodes import text_to_textnodes

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_text_nodes_conversion(self):

        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        result = text_to_textnodes(text)
        self.assertEqual(result, [TextNode("This is ", text_type_text),
                                TextNode("text", text_type_bold),
                                TextNode(" with an ", text_type_text),
                                TextNode("italic", text_type_italic),
                                TextNode(" word and a ", text_type_text),
                                TextNode("code block", text_type_code),
                                TextNode(" and an ", text_type_text),
                                TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
                                TextNode(" and a ", text_type_text),
                                TextNode("link", text_type_link, "https://boot.dev"),
        ])

  

 