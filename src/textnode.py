from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

#    except: ValueError:
#        print(f"That is not a known text type")



    
    
'''
Normal text
**Bold text**
_Italic text_
`Code text`
Links, in this format: [anchor text](url)
Images, in this format: ![alt text](url)
'''
    

class TextNode:
    
    
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, second_object):
        if self.text == second_object.text and self.text_type == second_object.text_type and self.url == second_object.url:
            return True
        
    def __repr__(self):
        
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    
    
    
    