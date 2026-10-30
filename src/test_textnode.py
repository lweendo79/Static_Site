import unittest
from textnode import TextNode, TextType
from textnode import text_node_to_html_node

class TestTextNode(unittest.TestCase):

    def setUp(self):
        self.node = TextNode("This is a text node", TextType.BOLD)
        self.node2 = TextNode("This is a text node", TextType.BOLD)
        self.node3= TextNode("This is a different text node", TextType.ITALIC)
        self.node4=TextNode("This is a text node",TextType.BOLD,"https://www.example.com")
        self.node5=TextNode(  "This is a text node",TextType.BOLD,"https://www.google.com")
      

    def test_eq(self):
        self.assertEqual(self.node, self.node2)


    def test_not_eq(self):
        self.assertNotEqual(self.node,self.node3)

    def test_url_default(self):
        self.assertIsNone(self.node.url)


    def test_url_provided(self):
        self.assertNotEqual(self.node4,self.node5)


    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        

        



if __name__ == "__main__":
    unittest.main()