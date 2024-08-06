from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from split_nodes_delimiter import split_nodes_delimiter
from extract_markdown import extract_markdown_images, extract_markdown_links
import re


def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    result = text_node_to_html_node(node)
    print(result)


def text_node_to_html_node(text_node):     

    if text_node.text_type == "text":          
        return convert_text(text_node)            
    elif text_node.text_type == "bold":            
        return convert_bold(text_node)            
    elif text_node.text_type == "italic":     
        return convert_italic(text_node)
    elif text_node.text_type == "code":
        return convert_code(text_node)
    elif text_node.text_type == "link":            
        return convert_link(text_node)
    elif text_node.text_type == "image": 
        return convert_image(text_node)
    else:
        Exception("Invalid text type")
        
# text_node: TextNode("This is a text node", "bold", "https://www.boot.dev")
def convert_text(text_node):
    # return leafnode object with text

    text = f"{text_node.text}" 
    converted_text = LeafNode(text)
    return converted_text

def convert_bold(text_node):
    # return leafnode object <b>text</b>

    text = f"{text_node.text}"
    converted_text = LeafNode("b", text)
    return converted_text

def convert_italic(text_node):
    # return <i>text</i>

    text = text_node.text
    converted_text = f"<i>{text}</i>"
    return converted_text

def convert_code(text_node):
    # return code tag text

    text = text_node.text
    converted_text = f"<code>{text}</code>"
    return converted_text

def convert_link(text_node):
    # return <a href="hi.com">text</a>
    text = text_node.text
    url = text_node.url

    converted_text = f'<a href="{url}">{text}</a>'
    return converted_text

def convert_image(text_node):
    # <img> empty string "src" and "alt" props ("src" is the image URL, "alt" is the alt text </img>
    url = text_node.url
    text = text_node.text

    converted_text = f'<img src="{url}" alt="{text}"></img>'
    return converted_text



if __name__ == "__main__":
    main()