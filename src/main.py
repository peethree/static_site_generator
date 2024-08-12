from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_node_to_html_node import text_node_to_html_node
from split_nodes_delimiter import split_nodes_delimiter
from extract_markdown import extract_markdown_images, extract_markdown_links
from split_nodes import split_nodes_image, split_nodes_link
from markdown_to_html_node import markdown_to_html_node
import os
import re
import shutil


def main():
    # remove public if it exists
    if os.path.exists("public"):
        shutil.rmtree("public")      

    if os.path.exists("static"):
        # get the files in static
        list_of_paths = dig_for_files("static")       

    # copy over static files to public
    for path in list_of_paths:     
        relative_path = os.path.relpath(path, "static")               
        destination_path = os.path.join("public", relative_path)

        # make directories if they don't exist (public, public/images/)
        os.makedirs(os.path.dirname(destination_path))                
        shutil.copy(path, destination_path)


def dig_for_files(dir):    

    file_paths = []

    for item in os.listdir(dir):
        # ['index.css, images]
        item_path = os.path.join(dir, item)
        # static/index.css, static/images/

        # base case: current path leads to a file
        if os.path.isfile(item_path):
            file_paths.append(item_path)

        # if it's directory, recursively call dig_for_files to reach the file
        if os.path.isdir(item_path):
            # [static/images]
            file_paths.extend(dig_for_files(item_path))  

    return file_paths     


if __name__ == "__main__":
    main()