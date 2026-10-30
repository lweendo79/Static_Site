from markdown_blocks import markdown_to_html_node

import os


def extract_title(markdown):
    lines=markdown.splitlines()



    for line in lines:
        if line.startswith("# "):
            return line.lstrip("#").strip()

    raise Exception("No H1 line matched")



def generate_page(from_path, template_path, dest_path):
    print (f" Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r' ,encoding='utf-8') as f:
      markdown_content=f.read()

    with open(template_path, 'r' , encoding='utf-8') as f:
        template=f.read()

    node =markdown_to_html_node(markdown_content)
    html_string=node.to_html()

    title=extract_title(markdown_content)

    template=template.replace("{{ Title }}",title)
    template=template.replace("{{ Content }}",html_string)

    dest_dir=os.path.dirname(dest_path)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir,exist_ok=True)


    with open(dest_path, 'w' , encoding='utf-8')as f:
        f.write(template)



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

     crawl_dir=os.listdir(dir_path_content)


     for file_name in crawl_dir:
        full_source_path=os.path.join(dir_path_content, file_name)
        dest_path=os.path.join(dest_dir_path,file_name)

        if os.path.isfile(full_source_path):
            if file_name.endswith(".md"):
                dest_html_path=dest_path[:-3] + ".html"
            
                generate_page(full_source_path ,template_path,dest_html_path)

        else:
           generate_pages_recursive(full_source_path,template_path,dest_path)






    