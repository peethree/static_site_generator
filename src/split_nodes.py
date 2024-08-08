from extract_markdown import extract_markdown_images, extract_markdown_links
from textnode import TextNode
import re

text_type_text = "text"
text_type_link = "link"
text_type_image = "image"

def split_nodes_image(old_nodes):
    """
    takes a list of old nodes as input, extracts each node's text value. 
    based on markdown image syntax pattern it splits the text with max split of 1.
    so there's only 1 string on each side of the split delimiter.The middle index of 
    the result of the split will be our image. For every set of (alt_text, url), 
    append a TextNode with the regular text part at index 0 to new_nodes list only if it
    is not an empty string. Then append the image TextNode and lastly the third item in the 
    sections list. After this update text_value to that of the remaining string.    
    """

    new_nodes = []

    for node in old_nodes:        
        text_value = node.text
        alt_texts_and_urls = extract_markdown_images(text_value)

        if alt_texts_and_urls:
            
            for alt_text, url in alt_texts_and_urls:
                sections = text_value.split(f"![{alt_text}]({url})", 1)

                if len(sections) != 2:
                    raise Exception("invalid markdown")
                
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], text_type_text))
                
                new_nodes.append(TextNode(alt_text, text_type_image, url))

                # update the text_value to the remaining part of the string
                text_value = sections[1]

            # add remaining text after the image if it's not an empty string
            if text_value != "":
                new_nodes.append(TextNode(text_value, text_type_text))
        else:
            # no images found with extract_markdown, add the original node instead
            new_nodes.append(node)

    return new_nodes
        

def split_nodes_link(old_nodes):  

    new_nodes = []

    for node in old_nodes:        
        text_value = node.text
        anchor_text_and_href = extract_markdown_links(text_value)

        if anchor_text_and_href:
            
            for anchor_text, href in anchor_text_and_href:
                sections = text_value.split(f"[{anchor_text}]({href})", 1)

                if len(sections) != 2:
                    raise Exception("invalid markdown")
                
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], text_type_text))
                
                new_nodes.append(TextNode(anchor_text, text_type_link, href))

                # update the text_value to the remaining part of the string
                text_value = sections[1]

            # add remaining text after the image if it's not an empty string
            if text_value != "":
                new_nodes.append(TextNode(text_value, text_type_text))
        else:
            # no images found with extract_markdown, add the original node instead
            new_nodes.append(node)

    return new_nodes

# old_nodes = [TextNode("This is text with a link to [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
#         "text"), TextNode("This is text with an image ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", "text")
#         ]

# print(split_nodes_link(old_nodes))

# always check images first




