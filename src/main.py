import sys
from textnode import TextNode
from textnode import TextType
from copystatic import copy_files_recursive
from copystatic import copy_files_to_public
from gencontent import generate_pages_recursive

def main():
     
     copy_files_to_public("static", "public")
     generate_pages_recursive("content","template.html","public")




if __name__ == "__main__":
    main()

