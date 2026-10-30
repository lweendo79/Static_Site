from textnode import TextNode, TextType
import re




def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type !=  TextType.TEXT:
            new_nodes.append(node)

        else:
           parts= node.text.split(delimiter)
           if len(parts)%2==0:
                raise ValueError(f"Unmatched delimiter '{delimiter}' in text: {node.text}")

           for i, part in enumerate(parts):
               if part=="":
                   continue
               if i%2==0:
                   new_nodes.append(TextNode(part, TextType.TEXT))
               else:
                   new_nodes.append(TextNode(part, text_type))

    return new_nodes


def extract_markdown_images(text):
    
    pattern=r"!\[([^\[\]]*)\]\((.*?)\)"
    return re.findall(pattern,text)

def extract_markdown_links(text):
    pattern=r"(?<!!)\[([^\[\]]*)\]\((.*?)\)"

    return re.findall(pattern,text)

            
def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes=[]

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts=extract_markdown_images(node.text)
        if not parts:
            new_nodes.append(node)
            continue
        remaining_text=node.text
        for alt_text, url in parts: 
            sections=remaining_text.split(f"![{alt_text}]({url})",maxsplit=1)

            if sections[0]!="": 
                new_nodes.append(TextNode(sections[0], TextType.TEXT)) 
            new_nodes.append(TextNode(alt_text,TextType.IMAGE,url=url))

            remaining_text=sections[1] 
        if remaining_text!="":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

           

           

    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes=[]

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts=extract_markdown_links(node.text)
        if not parts:
            new_nodes.append(node)
            continue
        remaining_text=node.text
        for link_text, url in parts: 
            sections=remaining_text.split(f"[{link_text}]({url})",maxsplit=1)

            if sections[0]!="": 
                new_nodes.append(TextNode(sections[0], TextType.TEXT)) 
            new_nodes.append(TextNode(link_text,TextType.LINK,url=url))

            remaining_text=sections[1] 
        if remaining_text!="":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    nodes = [node]
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes



