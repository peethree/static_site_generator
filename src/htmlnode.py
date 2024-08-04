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
        # if value is None:
            # raise Exception("value required")        
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
      
