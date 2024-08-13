from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
from generate_page import generate_page
import os


def generate_page_recursively(dir_path_content, template_path, dest_dir_path):  
    """recursive function for generation pages"""   

    print("Generating pages . . .") 

    # Crawl every entry in the content directory
    if os.path.isdir(dir_path_content):
        markdown_files = dig_for_files(dir_path_content) 
        # ['./content/index.md', './content/majesty/index.md']      

    # For each markdown file found, 
    for file_path in markdown_files:        
        dest_dir_path = file_path.replace("./content/", "./public/").replace("md", "html")
        # "./content/index.md" --> "./public/index.html"

        generate_page(file_path, "./template.html", dest_dir_path)


def dig_for_files(dir):    
    """
    recursive function for crawling through a directory and returning every file path.
    """

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




    