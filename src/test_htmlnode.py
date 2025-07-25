import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode



class TestHTMLNode(unittest.TestCase):
    def test_1(self):
        node_1 = HTMLNode(None, None, None, {"test" : "test thing"})
        node_2 = HTMLNode(None, None, None, {"test" : "test thing"})
        self.assertEqual(node_1.props_to_html(), node_2.props_to_html())


    def test_2(self):
        node_1 = HTMLNode(None, None, None, {"test 1" : "test thing 1",
                                             "test 2" : "test thing 2", 
                                             "test 3" : "test thing 3",
                                             "test 4" : "test thing 4"})
        node_2 = HTMLNode(None, None, None, {"test 1" : "test thing 1",
                                             "test 2" : "test thing 2",
                                             "test 3" : "test thing 3",
                                             "test 4" : "test thing 4"})
        self.assertEqual(node_1.props_to_html(), node_2.props_to_html())


    def test_3(self):
        node_1 = HTMLNode(None, None, None, {"test 1" : "test thing 1",
                                             "test 2" : "test thing 2",
                                             "test 3" : "test thing 3",
                                             "test 4" : "test thing 4"})
        node_2 = HTMLNode(None, None, None, {"test a" : "test thing a",
                                             "test b" : "test thing b",
                                             "test c" : "test thing c",
                                             "test d" : "test thing d"})
        self.assertNotEqual(node_1.props_to_html(), node_2.props_to_html())



class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Google", {"href" : "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Google</a>")





class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )






