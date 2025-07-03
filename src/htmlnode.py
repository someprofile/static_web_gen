class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        result = ""
        if self.props == None:
            result = f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            result = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
        
        #result = f"<{self.tag}{self.props_to_html}>{self.value}</{self.tag}>"
        
        
        return result

        #return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def props_to_html(self):
        
        result = ""

        for obj in self.props:
            result += f" {obj}=\"{self.props[obj]}\""


        
        return result
    

    def __repr__(self):
        #print(self)
        print(self.tag)
        print(self.value)
        print(self.children)
        print(self.props)






class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)



    def to_html(self):
        if self.value == None:
            raise ValueError
        
        if self.tag == None:
            return f"{self.value}"

        return super().to_html()

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"