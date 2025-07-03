class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError
    
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




