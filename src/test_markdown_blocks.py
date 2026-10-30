import unittest
from markdown_blocks import markdown_to_blocks, markdown_to_html_node
from markdown_blocks import block_to_block_type, BlockType

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )



    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Subheading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Sub-subheading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("#### Sub-sub-subheading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("##### Sub-sub-sub-subheading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Sub-sub-sub-sub-subheading"), BlockType.HEADING)

        self.assertEqual(block_to_block_type("```\nCode block\n```"), BlockType.CODE)

        self.assertEqual(block_to_block_type("> This is a quote\n> spanning multiple lines"), BlockType.QUOTE)

        self.assertEqual(block_to_block_type("- Item 1\n- Item 2\n- Item 3"), BlockType.UNORDERED_LIST)

        self.assertEqual(block_to_block_type("1. First item\n2. Second item\n3. Third item"), BlockType.ORDERED_LIST)
   
    def test_block_to_block_paragraph(self):
        self.assertEqual(block_to_block_type("This is a simple paragraph."), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("This is another paragraph with multiple lines.\nIt should still be considered a single paragraph."), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("This is a paragraph with **bold** and _italic_ text."), BlockType.PARAGRAPH)


    def test_paragraphs(self):
     md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

     node = markdown_to_html_node(md)
     html = node.to_html()
     self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )


def test_codeblock(self):
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )

if __name__ == "__main__":
    unittest.main()