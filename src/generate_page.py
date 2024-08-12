from markdown_to_html_node import markdown_to_html_node
from htmlnode import HTMLNode
from extract_title import extract_title
import os


def generate_page(from_path, template_path, dest_path):    
    print("Generating page from from_path to dest_path using template_path")

    # Read the markdown file at from_path and store the contents in a variable.

    with open(from_path, "r") as file:
        markdown_content = file.read()                 

    # Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.
    html_nodes = markdown_to_html_node(markdown_content)       
    markdown_html_string = html_nodes.to_html()   

    return markdown_html_string

    # # Use the extract_title function to grab the title of the page.
    # title = extract_title(markdown_content)            
   
    # # Read the template file at template_path and store the contents in a variable.
    # with open(template_path, "r") as file:
    #     template = file.read()

    # # replace placeholders
    # rendered = template.replace("{{ Title }}", title).replace("{{ Content }}", markdown_html_string)

    # # Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist.    
    # os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    # with open(dest_path, "w") as file:
    #     file.write(rendered)





    