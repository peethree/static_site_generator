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
            return new_nodes       
    
        
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
        
        section_nodes = []

        for i in range(len(sections)):
            # in case of empty string, skip over it 
            if sections[i] == "":
                continue            
            if i % 2 == 0:
                section_nodes.append(TextNode(sections[i], text_type_text))
            else:
                section_nodes.append(TextNode(sections[i], text_type))
        
        # preserve the order of the strings by extending
        new_nodes.extend(section_nodes)

    return new_nodes            


 
        



