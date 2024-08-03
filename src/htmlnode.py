class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):               

        # {
        #   "href": "https://www.google.com", 
        #   "target": "_blank",
        # } 

        # to

        #  href="https://www.google.com" target="_blank"

        attributes = []

        if self.props != None:
            for key, value in self.props.items():
                attributes.append(f'{key}="{value}"')

        return " ".join(attributes)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
