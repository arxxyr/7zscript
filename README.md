
# 文件解压工具

这个脚本可以帮助你批量解压带有密码的压缩文件（支持 ZIP、RAR 和 7Z 格式），并尝试使用一个密码列表来解锁这些文件。此外，它还可以重新压缩文件并去除密码，如果文件是非 7Z 格式，则在重新压缩后删除原文件。

## 功能

- 批量解压带密码的压缩文件。
- 支持多种文件格式：ZIP、RAR 和 7Z。
- 自动从密码列表中尝试密码。
- 重新压缩文件以去除密码。
- 删除原有的非 7Z 格式压缩文件。
- 跳过无需密码的文件。

## 安装指南

要使用这个脚本，你需要先安装必要的依赖。请按照以下步骤操作：

1. 确保你的系统已安装 Python。
2. 克隆或下载这个项目。
3. 创建并激活虚拟环境：
   
   - 在 Windows 上：
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

   - 在 Linux 上：
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

4. 在激活的虚拟环境中安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 使用说明

1. 准备一个文本文件（例如 `passwords.txt`），每行包含一个密码。
2. 确保你要处理的压缩文件位于同一个目录中。
3. 运行脚本，并通过命令行参数指定密码文件和文件夹路径。例如：

   ```bash
   python main.py --password_file=path/to/passwords.txt --folder=path/to/your/files
   ```

## 注意事项

- 确保你有合法权利访问和解压这些文件。
- 不支持破解未知密码的文件。
- 根据文件大小和数量，处理时间可能有所不同。
- 重要数据请备份后再使用。

## 许可

[MIT License](LICENSE)
