import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def setUp(self):
        self.node=HTMLNode(tag="div", value="Hello, World!", props={"class": "my-class", "id": "my-id"})
        self.node2=HTMLNode(tag="p", value="This is a paragraph.", props={"style": "color:red;"})
        self.node3=HTMLNode(tag="span", value="This is a span.", props=None)

    def test_props_to_html_multiple(self):
        self.assertEqual(self.node.props_to_html(), ' class="my-class" id="my-id"')

    def test_props_to_html_single(self):
        self.assertEqual(self.node2.props_to_html(), ' style="color:red;"')

    def test_props_to_html_none(self):
        self.assertEqual(self.node3.props_to_html(), '')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

   

if __name__ == "__main__":
    unittest.main()