import argparse
import os

argparse = argparse.ArgumentParser()
argparse.add_argument("-d", "--dir", dest = "dir")

args = argparse.parse_args()

global folder
folder = args.dir or "."

def index(source):
    list = []
    
    for root, dirs, files in os.walk(source):
        relroot = os.path.abspath(os.path.join(source))
        dir = os.path.relpath(root, relroot)

        for file in files:
            filename = os.path.join(root, file)

            if os.path.isfile(filename):
                relative = os.path.join(os.path.relpath(root, relroot), file)      
                
                if relative.endswith(".html") and not relative.startswith("."):
                    list.append(relative)
                
    return list

if __name__ == "__main__":
    files = index(folder);
    
    global template
    with open("template.html") as f:
        template = f.readlines()
    
    for file in files:
        with open(file) as f:
            print("Reading " + file)