# main.py
from file_extractor import FileExtractor
from helpers import compress_and_cleanup, safe_rmtree
from tqdm import tqdm
import argparse
import os
import glob

def main():
    parser = argparse.ArgumentParser(description="Remove password from encrypted files.")
    parser.add_argument("--password_file", required=True, help="Path to the password file")
    parser.add_argument("--folder", required=True, help="Path to the folder with encrypted files")
    args = parser.parse_args()

    tmp_folder = os.path.abspath("./tmp")
    safe_rmtree(tmp_folder)
    os.makedirs(tmp_folder, exist_ok=True)

    extractor = FileExtractor(args.password_file, tmp_folder)

    # 获取加密文件列表
    encrypted_files = [file for file in glob.glob(os.path.join(args.folder, "*")) if extractor.is_encrypted(file)]

    # 创建进度条
    progress_bar = tqdm(total=len(encrypted_files), desc="Processing")

    for file_path in encrypted_files:
        file_name = os.path.basename(file_path)
        if extractor.is_encrypted(file_path):
            if extractor.try_extract(file_path):
                new_file_path = os.path.splitext(file_path)[0] + ".7z" if not file_path.endswith(".7z") else file_path
                if compress_and_cleanup(tmp_folder, new_file_path) and new_file_path != file_path:
                    os.remove(file_path)
                    print(f"Removed original file: {file_name}")
            else:
                print(f"Failed to extract {file_name} with provided passwords.")
        else:
            print(f"Skipping unencrypted or unsupported file: {file_name}")
        progress_bar.update(1)

    safe_rmtree(tmp_folder)

if __name__ == "__main__":
    main()
