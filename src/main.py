from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from enum import Enum

def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node)

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

def text_node_to_html_node(text_node):
    # text_node: TextNode("This is a text node", "bold", "https://www.boot.dev")
    match text_node.text_type:
        case TextType.TEXT:            
            return convert_text(text_node)            
        case TextType.BOLD:            
            return convert_bold(text_node)            
        case TextType.ITALIC:            
            return convert_italic(text_node)
        case TextType.CODE:            
            return convert_code(text_node)
        case TextType.LINK:            
            return convert_link(text_node)
        case TextType.IMAGE:            
            return convert_image(text_node)
    raise Exception("Invalid text type")
        

def convert_text(text_node):
    # return leafnode text
    pass

def convert_bold(text_node):
    # return leafnode <b>text</b>
    pass

def convert_italic(text_node):
    # return <i>text</i>
    pass

def convert_code(text_node):
    # return code tag text
    pass

def convert_link(text_node):
    # return <a href="hi.com>text</a>"
    pass

def convert_image(text_node):
    # <img> empty string "src" and "alt" props ("src" is the image URL, "alt" is the alt text </img>
    pass






# class EditType(Enum):
#     NEWLINE = 1
#     SUBSTITUTE = 2
#     INSERT = 3
#     DELETE = 4

# # document: string, edit_type: EditType enum, edit: dict
# def handle_edit(document, edit_type, edit):
#     match edit_type:
#         case EditType.NEWLINE:
#             return new_line(document, edit)
#         case EditType.SUBSTITUTE:
#             return substitute(document, edit)
#         case EditType.INSERT:
#             return insert(document, edit)
#         case EditType.DELETE:
#             return delete(document, edit)

#     raise Exception("Unknown edit type")


if __name__ == "__main__":
    main()