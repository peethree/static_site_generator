import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_multiple_nodes(self):
        old_nodes = [TextNode("This is text with text", "text"), TextNode("and bold **text**", "text")]
        delimiter = "**"
        text_type = "bold"
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)

        self.assertEqual(result, [TextNode("This is text with text", "text"), TextNode("and bold ", "text"), TextNode("text", "bold")])

    def test_text_node(self):
        old_nodes = [TextNode("This is text with a ", "text")]
        delimiter = "**"
        text_type = "bold"
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)

        self.assertEqual(result, [TextNode("This is text with a ", "text")])

    def test_bold_delimeter(self):
        old_nodes = [TextNode("This is text with a **bold** word", "text")]
        delimiter = "**"
        text_type = "bold"
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)

        self.assertEqual(result, [TextNode("This is text with a ", "text"), TextNode("bold", "bold"), TextNode(" word", "text")])

    def test_italic_delimeter(self):
        old_nodes = [TextNode("This is text with an *italic* word", "text")]
        delimiter = "*"
        text_type = "italic"
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)

        self.assertEqual(result, [TextNode("This is text with an ", "text"), TextNode("italic", "italic"), TextNode(" word", "text")])

    def test_code_delimeter(self):
        old_nodes = [TextNode("This is text with a `code` block", "text")]
        delimiter = "`"
        text_type = "code"
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)

        self.assertEqual(result, [TextNode("This is text with a ", "text"), TextNode("code", "code"), TextNode(" block", "text")])

    def test_text_type(self):
        old_nodes = [TextNode("**text**", "bold")]
        delimiter = "**"
        text_type = "bold"
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)

        self.assertEqual(result, [TextNode("**text**", "bold")])

    def test_single_delimiter(self):    
        with self.assertRaises(Exception) as context:                       
            old_nodes = [TextNode("This is text with a `code block", "text")]
            delimiter = "`"
            text_type = "code"
            split_nodes_delimiter(old_nodes, delimiter, text_type)

        self.assertEqual(str(context.exception), "missing ending delimiter")

    def test_no_delimiter(self):    
        with self.assertRaises(Exception) as context:                       
            old_nodes = [TextNode("This is text with words", "text")]  
            delimiter = None          
            text_type = "text"
            split_nodes_delimiter(old_nodes, delimiter, text_type)

        self.assertEqual(str(context.exception), "invalid delimiter")

    def test_two_bold_delimeter(self):
        old_nodes = [TextNode("This is text **with** two **bold** words", "text")]
        delimiter = "**"
        text_type = "bold"
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)

        self.assertEqual(result, [TextNode("This is text ", "text"), TextNode("with", "bold"), TextNode(" two ", "text"), TextNode("bold", "bold"), TextNode(" words", "text")])