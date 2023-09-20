# Author: Gabriel das Neves
# Github: https://github.com/gabrieldasnevespinheiro

from zipfile import ZipFile, is_zipfile
# for rar files you need winrar installed, patoolib uses it.
import patoolib
import os


# Folder containing charts zip/rar files
scan_folder = "C:/Users/user/Downloads/charts"
# Clone hero songs folder
output_folder = "C:/Users/user/OneDrive/Documentos/Clone Hero/Songs"

def nemesis(): # delete all files if success
    for file in os.listdir(scan_folder):
        path = f"{scan_folder}/{file}"        
        os.remove(path)
    print("Input folder is cleaned.")

def extract() -> bool: # Returns True if success, False otherwise
    try:
        for file in os.listdir(scan_folder):
            path = f"{scan_folder}/{file}"
            
            if is_zipfile(path):
                with ZipFile(path, 'r') as zipObject:
                    name = file.replace("zip", "")
                    zipObject.extractall(path=f"{output_folder}/{name}")
                    
                    print(f"Sucessfully extracracted {file}")
            
            elif path.endswith('rar'): # for rar files
                name = file.replace(".rar", "")
                os.mkdir(f"{output_folder}/{name}")
                patoolib.extract_archive(path, outdir=f"{output_folder}/{name}")
                    
                print(f"Sucessfully extracracted {file}")
                    
        return True
    
    except Exception as e:
        print(f"a file extraction failed ")
        return False
    
res = extract()

if res:
    nemesis()
