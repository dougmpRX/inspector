import os
from datetime import datetime

DIRECTORY = '/mnt/c/Games'

def list_files_tree(directory):
    file_tree = {}
    for root, dirs, files in os.walk(directory):
        relative_path = os.path.relpath(root, directory)
        file_tree[relative_path] = []
        for filename in files:
            file_tree[relative_path].append(filename)
    return file_tree

def save_tree_to_file(file_tree, output_file):
    with open(output_file, 'w') as fp:
        for folder, files in file_tree.items():
            fp.write(f"{folder}\n")
            for filename in files:
                fp.write(f"  +-- {filename}\n")

if __name__ == "__main__":
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{timestamp}.txt"
    file_tree = list_files_tree(DIRECTORY)
    save_tree_to_file(file_tree, output_file)