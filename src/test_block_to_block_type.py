import unittest

from block_to_block_type import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_blocks_type(self):

        # headings
        result = block_to_block_type("# from")
        self.assertEqual(result, "heading")

        result = block_to_block_type("## big")
        self.assertEqual(result, "heading")

        result = block_to_block_type("### to")
        self.assertEqual(result, "heading")

        result = block_to_block_type("#### small")
        self.assertEqual(result, "heading")

        result = block_to_block_type("##### thumbs_up")
        self.assertEqual(result, "heading")

        result = block_to_block_type("###### emoji")
        self.assertEqual(result, "heading")

        # code blocks
        result = block_to_block_type("```beep-boop-bleep-bloop```")
        self.assertEqual(result, "code")  

        # quotes
        result = block_to_block_type(">misquoting a historical figure")
        self.assertEqual(result, "quote")       
   
        # unordered list
        result = block_to_block_type("* tomatoes\n* cucumber\n* avocado")
        self.assertEqual(result, "unordered list")
       
        # ordered list
        result = block_to_block_type("1. uno\n2. dos \n3. très")
        self.assertEqual(result, "ordered list")        

        # paragraphs
        result = block_to_block_type("multiple line\npargraph.")
        self.assertEqual(result, "paragraph")      
   