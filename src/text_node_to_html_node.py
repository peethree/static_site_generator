from htmlnode import LeafNode



def text_node_to_html_node(text_node):        

    if text_node.text_type == "text":          
        return convert_text(text_node)            
    elif text_node.text_type == "bold":            
        return convert_bold(text_node)            
    elif text_node.text_type == "italic":     
        return convert_italic(text_node)
    elif text_node.text_type == "code":
        return convert_code(text_node)
    elif text_node.text_type == "link":            
        return convert_link(text_node)
    elif text_node.text_type == "image": 
        return convert_image(text_node)
    else:
        Exception("Invalid text type")
        
# text_node: TextNode("This is a text node", "bold", "https://www.boot.dev")
def convert_text(text_node):       
    return LeafNode(None, text_node.text)

def convert_bold(text_node):    
    return LeafNode("b", text_node.text)

def convert_italic(text_node):      
    return LeafNode("i", text_node.text)

def convert_code(text_node):  
    return LeafNode("code", text_node.text)

def convert_link(text_node):    
    return LeafNode("a", text_node.text, {"href": text_node.url})

def convert_image(text_node):
    return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})