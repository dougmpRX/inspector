import os
import re

class FilenameHandler:
    def __init__(self, directory):
        self.directory = directory

    def rename_files(self):
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                filename, extension = os.path.splitext(file)
                name, number = filename[:10], filename[11:]
                if re.match(r'^\d$', name[0]): # testa se apenas o primeiro caractere é um número
                    new_filename = f"{number} {name}{extension}"
                    old_path = os.path.join(root, file)
                    new_path = os.path.join(root, new_filename)
                    self.rename_file(old_path, new_path)
                else:
                    print(f"Arquivo ignorado: {file}")

    def rename_file(self, old_path, new_path):
        os.rename(old_path, new_path)
