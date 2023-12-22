# helpers.py
import subprocess
import shutil
import os
import time


def compress_and_cleanup(source_folder, destination_file):
    # 构建 7z 命令来压缩文件
    command = ["7z", "a", "-t7z", "-y", destination_file, os.path.join(source_folder, '*')]

    # 尝试执行压缩命令
    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"Compressed to {destination_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during compression: {e}")
        return False

    # 尝试删除临时文件夹
    try:
        shutil.rmtree(source_folder)
    except OSError as e:
        print(f"Error deleting temporary folder: {e}. Retrying...")
        time.sleep(1)  # 稍等一秒后再次尝试删除
        try:
            shutil.rmtree(source_folder)
        except OSError as e:
            print(f"Second attempt to delete temporary folder failed: {e}")
            return False

    return True

def safe_rmtree(path, retries=2, delay=1):
    """
    尝试安全地删除指定的路径。
    :param path: 要删除的路径。
    :param retries: 删除操作的重试次数。
    :param delay: 重试前的等待时间（秒）。
    """
    while retries > 0:
        try:
            shutil.rmtree(path)
            break
        except OSError as e:
            print(f"Error deleting {path}: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
            retries -= 1
            if retries == 0:
                print(f"Failed to delete {path} after several attempts.")