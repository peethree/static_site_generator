from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_node_to_html_node import text_node_to_html_node
from split_nodes_delimiter import split_nodes_delimiter
from extract_markdown import extract_markdown_images, extract_markdown_links
from split_nodes import split_nodes_image, split_nodes_link
import re


def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    result = text_node_to_html_node(node)
    print(result)



if __name__ == "__main__":
    main()