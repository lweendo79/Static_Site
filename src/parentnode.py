from htmlnode import HTMLNode


class ParentNode(HTMLNode):

    def __init__(self,tag,children,props=None):
        super().__init__(tag, value=None,children=children,props=props)



    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag cannot be None")
        if self.children is None:
            raise ValueError("Children cannot be None")

        return f"<{self.tag}{self.props_to_html()}>{''.join(child.to_html() for child in self.children)}</{self.tag}>"
    