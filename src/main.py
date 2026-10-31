import sys
from textnode import TextNode
from textnode import TextType
from copystatic import copy_files_recursive
from copystatic import copy_files_to_public
from gencontent import generate_pages_recursive

def main():
     
     basepath="/"
     if len(sys.argv)>1:
          basepath=sys.argv[1]

     copy_files_to_public("static", "docs")
     generate_pages_recursive("content","template.html","docs",basepath)




if __name__ == "__main__":
    main()

