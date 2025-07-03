import unittest
from htmlnode import HTMLNode


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