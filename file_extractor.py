# file_extractor.py
import subprocess
import os

class FileExtractor:
    def __init__(self, password_file, tmp_folder):
        self.tmp_folder = tmp_folder
        self.passwords = self.read_passwords(password_file)

    @staticmethod
    def read_passwords(password_file):
        with open(password_file, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file]

    def is_encrypted(self, file_path):
        command = ["7z", "l", "-slt", file_path]
        try:
            result = subprocess.run(command, check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return "Encrypted = +" in result.stdout
        except subprocess.CalledProcessError:
            return False

    def try_extract(self, file_path):
        for password in self.passwords:
            command = ["7z", "x", f"-p{password}", "-aoa", f"-o{self.tmp_folder}", file_path]
            try:
                result = subprocess.run(command, check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if "Everything is Ok" in result.stdout:
                    print(f"Extracted {file_path} with password: {password}")
                    return True
            except subprocess.CalledProcessError:
                continue
        return False
