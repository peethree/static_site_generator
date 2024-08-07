from extract_markdown import extract_markdown_images, extract_markdown_links
from textnode import TextNode
import re


def split_nodes_image(old_nodes):
    """takes an old node as input, extracts its text value. 
    based on markdown image syntax pattern it splits the text.
    try to apply extract_markdown function and append its result to a list.
    filter out any empty lists that resulted from empty strings"""

    new_nodes = []

    for node in old_nodes:
        text_value = node.text

        new_list = [] 

        pattern = r"(\!\[.*?\]\(.*?\))"  

        text_type_text = "text"
        text_type_image = "image"

        sequence = re.split(pattern, text_value)

        for seq in sequence:
            try:
                new_seq = extract_markdown_images(seq)
                new_list.append(new_seq)
            except:
                new_list.append(seq)

        filtered_list = []
        
        for item in new_list:
            # remove empty lists from the result
            if item != []:            
                filtered_list.append(item)

        

        for item in new_list:
            # if item is regular text and not empty, turn it into a textnode    
            if item != None and not isinstance(item, list):
                
                node = TextNode(item, text_type_text)
                new_nodes.append(node)

            # if item is an instance of a tuple, then it's a link --> first item in tuple is anchor text, 
            if isinstance(item, list) and len(item) == 1 and isinstance(item[0], tuple):
                
                alt_text, url = item[0]                     
                node = TextNode(alt_text, text_type_image, url)
                new_nodes.append(node)
        
    return new_nodes
        

def split_nodes_link(old_nodes):  
    new_nodes = []

    for node in old_nodes:
        text_value = node.text

        new_list = []   

        # pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"       
        pattern = r"(\[.*?\]\(.*?\))"   

        text_type_text = "text"
        text_type_link = "link"
        
        sequence = re.split(pattern, text_value)   
        # ['This is text with a link ', '[to boot dev](https://www.boot.dev)', ' and' '[to youtube](https://www.youtube.com/@bootdotdev)']
        
        for seq in sequence:
            try:
                new_seq = extract_markdown_links(seq)
                new_list.append(new_seq)
            except:
                new_list.append(seq)

        filtered_list = []
        
        for item in new_list:
            # remove empty lists from the result
            if item != []:            
                filtered_list.append(item)

        

        for item in new_list:
            # if item is regular text and not empty, turn it into a textnode    
            if item != None and not isinstance(item, list):
                
                node = TextNode(item, text_type_text)
                new_nodes.append(node)

            # if item is an instance of a tuple, then it's a link --> first item in tuple is anchor text, 
            if isinstance(item, list) and len(item) == 1 and isinstance(item[0], tuple):
                # item = [('to boot dev', 'https://www.boot.dev')]
                anchor_text, url = item[0]                     
                node = TextNode(anchor_text, text_type_link, url)
                new_nodes.append(node)                   
    
    
    return new_nodes



# text_value = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
# always check images first




