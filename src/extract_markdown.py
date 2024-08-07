import re

def extract_markdown_images(text):

    list_of_images = []

    if text:
        images = re.findall(r"!\[(.*?)\]\((.*?)\)", text)

        if images:

            for image in images:
                alt_text, url = image
                image_tuple = (alt_text, url)
                list_of_images.append(image_tuple)
        else:
            return text

    return list_of_images

    

def extract_markdown_links(text):

    list_of_links = []

    if text:
        links = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

        if links:

            for link in links:            
                anchor_text, url = link
                image_tuple = (anchor_text, url)
                list_of_links.append(image_tuple)
        else:
            return text

    return list_of_links


