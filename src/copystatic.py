import os
import shutil
from pathlib import Path





def copy_files_recursive(source_dir_path,dest_dir_path):
    
    
        for item in os.listdir(source_dir_path):
            src_path=os.path.join(source_dir_path, item)
            dst_path=os.path.join(dest_dir_path, item)

            if os.path.isfile (src_path):
                print(f"Copying file: {src_path} -> {dst_path}")
                shutil.copy(src_path,dst_path)

            else:
                os.mkdir(dst_path)

                copy_files_recursive(src_path,dst_path)
            

def copy_files_to_public (source_dir_path,dest_dir_path):
    if os.path.exists(dest_dir_path):
         shutil.rmtree(dest_dir_path) 

   
    os.mkdir(dest_dir_path)
    copy_files_recursive(source_dir_path,dest_dir_path)
    
