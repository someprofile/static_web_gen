import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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


class TestHTMLConversion(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_url(self):
        node = TextNode("Testing for url", TextType.IMAGE, "google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "Testing for url")
        self.assertEqual(html_node.props, {
            "src" : "google.com",
            "alt" : "Testing for url"
            })
        
    def test_url2(self):
        node = TextNode("Testing for url in bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Testing for url in bold")
        self.assertEqual(html_node.props, None)





if __name__ == "__main__":
    unittest.main()