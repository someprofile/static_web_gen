import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    
    
    def test_eq_2(self):
        node = TextNode("This is a text node", TextType.CODE, "https://www.weewoo.com")
        node2 = TextNode("This is a text node", TextType.CODE, "https://www.weewoo.com")
        self.assertEqual(node, node2)
    

    def test_not_eq_1(self):
        node = TextNode("This is not a text node", TextType.CODE, "https://www.weewoo.com")
        node2 = TextNode("This is a text node", TextType.CODE, "https://www.weewoo.com")
        self.assertNotEqual(node, node2)

    
    def test_not_eq_2(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.weewoo.com")
        node2 = TextNode("This is a text node", TextType.CODE, "https://www.weewoo.com")
        self.assertNotEqual(node, node2)


    def test_not_eq_3(self):
        node = TextNode("This is a text node", TextType.CODE, "https://www.woogle.com")
        node2 = TextNode("This is a text node", TextType.CODE, "https://www.weewoo.com")
        self.assertNotEqual(node, node2)


    def test_not_eq_4(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.CODE, "https://www.weewoo.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()