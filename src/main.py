from textnode import TextNode
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
            # return leafnode raw text
            pass
        case TextType.BOLD:
            # return leafnode <b>text</b>
            pass
        case TextType.ITALIC:
            # return <i>text</i>
            pass
        case TextType.CODE:
            # return code tag text
            pass
        case TextType.LINK:
            # return <a href="hi.com>text</a>"
            pass
        case TextType.IMAGE:
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