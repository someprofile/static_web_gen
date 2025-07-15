from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


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
    
    



def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise ValueError("This is not a TextNode.")
    
    
    tag_dict = {
        TextType.TEXT : None,
        TextType.BOLD : "b",
        TextType.ITALIC : "i",
        TextType.CODE : "code",
        TextType.LINK : "a",
        TextType.IMAGE : "img"
        }

    prop_dict = {
        TextType.TEXT : None,
        TextType.BOLD : None,
        TextType.ITALIC : None,
        TextType.CODE : None,
        TextType.LINK : {
            "href" : text_node.url
            },
        TextType.IMAGE : {
            "src" : text_node.url,
            "alt" : text_node.text
            }

    }

    return LeafNode(tag_dict[text_node.text_type], text_node.text, prop_dict[text_node.text_type])
    
    
    