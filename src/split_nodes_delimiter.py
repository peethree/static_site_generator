from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # does not work for multiple instances of the same delimiter TODO:

    new_list = []

    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"    

    for node in old_nodes:        

        if text_type != text_type_text:
            new_list.append(node)
            return new_list

        # If a matching closing delimiter is not found, 
        # raise an exception.
        text_content = node.text

        try:
            delimiter_count = text_content.count(delimiter)
        except:
            raise Exception("no delimiter given")
            
        if delimiter_count == 0:
            new_list.append(node)
        if delimiter_count == 1:
            raise Exception("invalid markdown, ending delimiter not found")
        
        if delimiter_count == 2:
            sections = text_content.split(delimiter)

            # this is a **test**"
            # sections = ['this is a ', 'test', '']

            # this **is** a test
            # ['this ', 'is', ' a test']

            # **this** is a test
            # ['', 'this', ' is a test']

            part_before_delimiter = sections[0]
            part_between_delimiter = sections[1]
            part_after_delimiter = sections[2]

            # TextNode does not support empty string, so only add when it has an actual value
            if part_before_delimiter != "":
                new_list.append(TextNode(part_before_delimiter, text_type_text))

            if delimiter == "**":
                t_type = text_type_bold
            if delimiter == "*":
                t_type = text_type_italic
            if delimiter == "```":
                t_type = text_type_code            
            
            new_list.append(TextNode(part_between_delimiter, t_type))

            # same here as for part_before_delimiter
            if part_after_delimiter != "":
                new_list.append(TextNode(part_after_delimiter, text_type_text))

    return new_list




            




 
        



