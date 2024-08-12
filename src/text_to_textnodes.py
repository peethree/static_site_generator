from textnode import TextNode

from split_nodes_delimiter import split_nodes_delimiter
from split_nodes import split_nodes_image, split_nodes_link

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def text_to_textnodes(text):
    """
    takes text as input and splits it into TextNodes.
    sequentially uses the split functions.
    """
    node = [TextNode(text, text_type_text)]    

    # bold: delimiter **, text_type_bold    
    nodes = split_nodes_delimiter(node, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)    
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes       

# text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"


# text = "**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)"
# print(text_to_textnodes(text))