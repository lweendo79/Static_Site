import unittest

from inline_markdown import split_nodes_delimiter,extract_markdown_images,extract_markdown_links, split_nodes_image ,split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold(self):
      node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
      new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
      self.assertListEqual(
        new_nodes,
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT),
        ],
    )
       
    def test_italic(self):
        node = TextNode("This is text with an *italicized phrase* in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italicized phrase", TextType.ITALIC),
                TextNode(" in the middle", TextType.TEXT),
            ],
        )

    def test_unmatched_delimiter(self):
        node = TextNode("This is text with an *unmatched delimiter in the middle", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "*", TextType.ITALIC)

    
    def test_extract_markdown_images_standard(self):
        """Test standard behavior with multiple valid images."""
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [
            ('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), 
            ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')
        ]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links_standard(self):
        """Test standard behavior with multiple valid hyperlinks."""
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [
            ('to boot dev', 'https://www.boot.dev'), 
            ('to youtube', 'https://www.youtube.com/@bootdotdev')]

        self.assertEqual(extract_markdown_links(text), expected)




    def test_split_nodes_link(self):    
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, url="https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, url="https://www.youtube.com/@bootdotdev"),
            ],
        )
    def test_split_nodes_image(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("rick roll", TextType.IMAGE, url="https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" and ", TextType.TEXT),
                TextNode("obi wan", TextType.IMAGE, url="https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
        )


    def test_text_to_textnodes(self):
        text = "This is a simple text without *bolded phrase formatting."
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, text)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

    def test_text_to_textnodes_without_formatting(self):
        text = "This is a simple text without any formatting."
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, text)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

    def test_text_to_textnodes_with_mixture(self):
        text = "This is a **bolded phrase** and _italicized phrase_ in the middle."
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 5)
        self.assertEqual(nodes[0].text, "This is a ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "bolded phrase")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, " and ")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[3].text, "italicized phrase")
        self.assertEqual(nodes[3].text_type, TextType.ITALIC)
        self.assertEqual(nodes[4].text, " in the middle.")
        self.assertEqual(nodes[4].text_type, TextType.TEXT)

    

    