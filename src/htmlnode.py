

class  HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag=tag
        self.value=value
        self.children=children
        self.props=props


    def to_html(self):
        raise NotImplementedError("Subclasses must implement the to_html method.")

    def props_to_html(self):

        results = []
        if self.props is None:
            return ""
        for key, value in self.props.items():
            results.append(f' {key}="{value}"')
        return "".join(results)

    def __repr__(self):
        return f"HTMLNode(tag='{self.tag}', value='{self.value}', children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,children=None,props=props)
       
        

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        
        if self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(tag='{self.tag}',value='{self.value}',props={self.props})"

    


    

    
