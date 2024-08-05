class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError        

    def props_to_html(self):                 

        attributes = []

        if self.props != None:
            for key, value in self.props.items():
                attributes.append(f'{key}="{value}"')

        return " ".join(attributes)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
      
        super().__init__(tag, value, children=None, props=props)    


    def to_html(self):    

        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        
        if self.tag is None:
            return self.value
        else:
                        
            if self.props is None:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            # when additional properties are given
            # LeafNode("a", "Click me!", {"href": "https://www.google.com"})
            else:                
                for key, value in self.props.items():
                    k = key
                    v = value

                return f'<{self.tag} {k}="{v}">{self.value}</{self.tag}>'
            
    def __repr__(self):
        return f'LeafNode("{self.tag}", "{self.value}", "{self.props}")'
    
    def __eq__(self, other):
        if not isinstance(other, LeafNode):
            return False
        return (self.tag == other.tag and
                self.value == other.value and
                self.props == other.props)
            

class ParentNode(HTMLNode):
    # tag, value, child, props
    def __init__(self, tag=None, children=None, props=None):

        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode needs a tag")
        if self.children is None:
            raise ValueError("ParentNode needs to have a child")
        
        # opening tag
        html = f"<{self.tag}"
        
        # inject properties if given
        if self.props:
            html += " " + self.props_to_html()
        
        # end of opening tag
        html += ">"        
        
        for child in self.children:
            html += child.to_html()        
        
        html += f"</{self.tag}>"
        
        return html
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
            
      
            


