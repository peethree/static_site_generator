from htmlnode import HTMLNode, ParentNode, LeafNode
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from text_to_textnodes import text_to_textnodes
from textnode import TextNode
from text_node_to_html_node import text_node_to_html_node

# heading
# code
# quote
# unordered list
# ordered list


block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered list"
block_type_ordered_list = "ordered list"

def markdown_to_html_node(markdown):
    # split markdown into blocks
    new_nodes = []

    blocks = markdown_to_blocks(markdown)

    # loop over each block
    for block in blocks:
        # determine type
        type = block_to_block_type(block)

        # based on type: create new HTMLNode
        if type == block_type_paragraph:    
            lines = block.split("\n")   
            
            paragraph = " ".join(lines)     
            children = text_to_children(paragraph)

            new_nodes.append(ParentNode("p", None, children))

        if type == block_type_heading:
            if block.startswith("# "):
                block = block.lstrip("# ").strip()
                children = text_to_children(block)
                new_nodes.append(ParentNode("h1", None, children))
            elif block.startswith("## "):
                block = block.lstrip("## ").strip()
                children = text_to_children(block)
                new_nodes.append(ParentNode("h2", None, children))
            elif block.startswith("### "):
                block = block.lstrip("### ").strip()
                children = text_to_children(block)
                new_nodes.append(ParentNode("h3", None, children))
            elif block.startswith("#### "):
                block = block.lstrip("#### ").strip()
                children = text_to_children(block)
                new_nodes.append(ParentNode("h4", None, children))
            elif block.startswith("##### "):
                block = block.lstrip("##### ").strip()
                children = text_to_children(block)
                new_nodes.append(ParentNode("h5", None, children))
            elif block.startswith("###### "):
                block = block.lstrip("###### ").strip()
                children = text_to_children(block)
                new_nodes.append(ParentNode("h6", None, children))

        # code blocks surrounded by <code>, nested inside a <pre> tag
        if type == block_type_code:   
            block = block.strip().strip("`").strip("\n")  

            children = text_to_children(block)
            code_block = ParentNode("code", None, children)

            new_nodes.append(ParentNode("pre", None, [code_block]))
                
        if type == block_type_quote:
            
            # block = block.strip().strip("> ")       
            # children = text_to_children(block)
            # new_nodes.append(ParentNode("blockquote", None, children))

            lines = block.split("\n")

            new_lines = []

            for line in lines:
                # remove the ">"
                new_lines.append(line.lstrip(">").strip())

            text = " ".join(new_lines)
            children = text_to_children(text)

            new_nodes.append(ParentNode("blockquote", None, children))

        if type == block_type_unordered_list:
            lines = block.split("\n")

            list_items = []            
            
            for line in lines:               
            
                # remove "* " prefix
                line_text = line[2:]  
                line_children = text_to_children(line_text)                
                
                list_item_node = ParentNode("li", None, line_children)                
                
                list_items.append(list_item_node)        
           
            # surrounded by a <ul> tag, and each list item should be surrounded by a <li> tag
            unordered_list_node = ParentNode("ul", None, list_items)                        
            new_nodes.append(unordered_list_node)          
            
        if type == block_type_ordered_list:
            lines = block.split("\n")

            list_items = []            
            
            for line in lines:               
            
                # remove "1. " prefix
                line_text = line[3:]  
                line_children = text_to_children(line_text)                
                
                list_item_node = ParentNode("li", None, line_children)                
                
                list_items.append(list_item_node)        
           
            # surrounded by a <ol> tag, and each list item should be surrounded by a <li> tag
            unordered_list_node = ParentNode("ol", None, list_items)                        
            new_nodes.append(unordered_list_node)

    # make all the block nodes children under a single parent HTML node
    # (which should just be a div) and return it
    return ParentNode("div", None, new_nodes)   

    
def text_to_children(text):
    """
    It takes a string of text and returns a list of HTMLNodes 
    that represent the inline markdown using previously created functions 
    (think TextNode -> HTMLNode).  
    """

    text_nodes = text_to_textnodes(text)

    nodes = []
    for node in text_nodes:
        # expects a single node as input
        nodes.append(text_node_to_html_node(node))

    return nodes




   

