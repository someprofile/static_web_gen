class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        result = ""
        #print("master node test")

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

        #print("leafnode test")

        if self.value == None:
            raise ValueError
        
        if self.tag == None:
            return f"{self.value}"

        return super().to_html()

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    



class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)



    def to_html(self):
        if self.tag == None:
            raise ValueError("There is no tag. Is this a leaf?")

        if self.children == None:
            raise ValueError("There are no children in this node.")

        result = f"<{self.tag}>"
        
        for obj in self.children:
            if isinstance(obj, ParentNode):
                result += obj.to_html()

            if isinstance(obj, LeafNode):
                result += f"{LeafNode(obj.tag, obj.value).to_html()}"

        #print(obj == type(LeafNode)) 
        #print(isinstance(obj, LeafNode))   

        result += f"</{self.tag}>"


        return result
        
        
        
        




node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        ParentNode(
            "d", 
            [
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ]),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text")
    ],
)

print(node.to_html())



