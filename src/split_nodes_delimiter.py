from textnode import TextNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:        

        # If an "old node" is not a "text" type, just add it to the new list as-is
        if node.text_type != text_type_text:
            new_nodes.append(node)    
            continue                         
        
        valid_delimiters = ["**", "*", "`"]

        if delimiter not in valid_delimiters:
            raise Exception("invalid delimiter")

        sections = node.text.split(delimiter)      

        # this is a **test**"
        # sections = ['this is a ', 'test', '']

        # this **is** a test
        # ['this ', 'is', ' a test']

        # **this** is a test
        # ['', 'this', ' is a test']

        # the uneven index is the string closed in by delimiters

        # if the remainder of the split is not divisible by 2 then an uneven number of delimiters was found in the string
        if len(sections) % 2 == 0:
            raise Exception("missing ending delimiter")             

        for i, section in enumerate(sections):
            # in case of empty string, skip over it 
            if section == "":
                continue            
            if i % 2 == 0:
                new_nodes.append(TextNode(section, text_type_text))
            else:
                new_nodes.append(TextNode(section, text_type))             

    return new_nodes            


 
        



